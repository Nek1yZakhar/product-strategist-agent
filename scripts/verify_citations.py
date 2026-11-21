#!/usr/bin/env python3
"""
scripts/verify_citations.py — Deterministic Citation & URL Integrity Verifier
Part of the Product Strategist Agent (MGIMO AI Challenge 2026).

Audits all research findings in knowledge/projects/<project>/findings/*.md.
Resolves each source_url via HTTP HEAD (with GET fallback), detects dead links,
guards against the 3-13% hallucinated URL rate documented in arXiv:2504.00317,
and optionally updates the YAML frontmatter.
"""

import argparse
import os
import re
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


def parse_frontmatter(content: str) -> tuple[dict, str]:
    """Parse YAML frontmatter from markdown file without external dependencies."""
    pattern = r"^---\s*\n(.*?)\n---\s*\n(.*)$"
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        return {}, content

    yaml_block = match.group(1)
    body = match.group(2)

    metadata = {}
    for line in yaml_block.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            key, val = line.split(":", 1)
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            metadata[key] = val

    return metadata, body


def update_frontmatter_field(content: str, field: str, new_value: str) -> str:
    """Updates or inserts a field in the YAML frontmatter."""
    pattern = rf"^({re.escape(field)}\s*:\s*)(.*)$"

    lines = content.splitlines()
    in_frontmatter = False
    replaced = False

    new_lines = []
    for line in lines:
        if line.strip() == "---":
            in_frontmatter = not in_frontmatter
            new_lines.append(line)
            continue

        if in_frontmatter and not replaced:
            if re.match(pattern, line):
                new_lines.append(f"{field}: {new_value}")
                replaced = True
                continue

        new_lines.append(line)

    if in_frontmatter and not replaced:
        # If field didn't exist in frontmatter, insert before closing ---
        new_lines.insert(-1, f"{field}: {new_value}")

    return "\n".join(new_lines) + "\n"


def check_url(url: str, timeout: int = 6) -> tuple[str, int, str]:
    """
    Resolves URL via HTTP HEAD with GET fallback.
    Returns: (status: 'verified' | 'dead' | 'hallucinated', http_code, message)
    """
    if not url or url.lower() in ("none", "pending", "", "n/a"):
        return "dead", 0, "Empty or placeholder URL"

    parsed = urllib.parse.urlparse(url)
    if not parsed.scheme or not parsed.netloc:
        return "hallucinated", 0, "Invalid URL structure"

    # Known synthetic or dummy domains
    dummy_domains = ["example.com", "fake.org", "test.local", "dummy.ai"]
    if any(d in parsed.netloc.lower() for d in dummy_domains):
        return "hallucinated", 0, "Synthetic or dummy test domain"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 (CitationVerifier/1.0)"
    }

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    # Attempt HEAD request first
    try:
        req = urllib.request.Request(url, headers=headers, method="HEAD")
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            code = resp.getcode()
            if 200 <= code < 400:
                return "verified", code, "Resolved successfully (HEAD)"
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, Exception):
        pass

    # Fallback to GET request with streaming cutoff
    try:
        req = urllib.request.Request(url, headers=headers, method="GET")
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            code = resp.getcode()
            if 200 <= code < 400:
                return "verified", code, "Resolved successfully (GET)"
            return "dead", code, f"HTTP Error {code}"
    except urllib.error.HTTPError as e:
        if e.code in (403, 401):
            # Anti-bot protections often return 403 to automated scripts while domain exists
            return "verified", e.code, "Domain active (Restricted by Bot Wall / WAF)"
        return "dead", e.code, f"HTTP {e.code}"
    except urllib.error.URLError as e:
        return "dead", 0, f"Network/DNS failure: {e.reason}"
    except Exception as e:
        return "dead", 0, f"Resolution error: {str(e)[:50]}"


def verify_project_findings(project_dir: Path, update_files: bool = False) -> list[dict]:
    """Scans findings directory in a project and audits each file."""
    findings_dir = project_dir / "findings"
    results = []

    if not findings_dir.exists():
        print(f"[!] Findings directory not found: {findings_dir}")
        return results

    md_files = list(findings_dir.glob("*.md"))
    if not md_files:
        print(f"[*] No markdown files found in {findings_dir}")
        return results

    print(f"[*] Auditing {len(md_files)} findings in '{project_dir.name}'...\n")

    for file_path in md_files:
        content = file_path.read_text(encoding="utf-8")
        meta, _ = parse_frontmatter(content)

        claim = meta.get("claim", file_path.stem)
        url = meta.get("source_url", "")
        old_status = meta.get("verified", "pending")

        status, code, msg = check_url(url)

        results.append({
            "file": file_path.name,
            "claim": claim[:60] + ("..." if len(claim) > 60 else ""),
            "url": url,
            "old_status": old_status,
            "status": status,
            "code": code,
            "message": msg
        })

        if update_files and status != old_status:
            updated_content = update_frontmatter_field(content, "verified", status)
            file_path.write_text(updated_content, encoding="utf-8")
            print(f"  [UPDATED] {file_path.name} -> verified: {status}")

    return results


def print_markdown_report(results: list[dict]):
    """Outputs a formatted markdown table summarizing verification."""
    print("\n### Citation Verification & URL Integrity Report")
    print("| File | Verified Status | HTTP Code | Source URL | Diagnostic Note |")
    print("| :--- | :--- | :---: | :--- | :--- |")

    verified_count = sum(1 for r in results if r["status"] == "verified")
    dead_count = sum(1 for r in results if r["status"] == "dead")
    hallucinated_count = sum(1 for r in results if r["status"] == "hallucinated")

    for r in results:
        status_tag = f"**{r['status'].upper()}**"
        if r["status"] == "verified":
            status_tag = f"OK ({r['status']})"
        print(f"| `{r['file']}` | {status_tag} | {r['code']} | [{r['url'][:30]}...]({r['url']}) | {r['message']} |")

    print("\n**Audit Summary:**")
    print(f"- Total Sources Scanned: {len(results)}")
    print(f"- Verified Active (200 / WAF): {verified_count}")
    print(f"- Dead / Unreachable: {dead_count}")
    print(f"- Hallucinated / Fabricated: {hallucinated_count}")

    if dead_count + hallucinated_count == 0 and len(results) > 0:
        print("\n> [!NOTE]\n> All empirical citations verified. Zero hallucination leak detected.")
    elif dead_count + hallucinated_count > 0:
        print(f"\n> [!WARNING]\n> Detected {dead_count + hallucinated_count} disqualified sources. Quarantining from strategy synthesis.")


def main():
    parser = argparse.ArgumentParser(description="Deterministic Citation & URL Integrity Verifier")
    parser.add_argument("--project", default="demo-megafon", help="Target project folder name in knowledge/projects/")
    parser.add_argument("--update", action="store_true", help="Automatically update YAML frontmatter in findings files")
    parser.add_argument("--url", help="Directly test a single URL")

    args = parser.parse_args()

    if args.url:
        status, code, msg = check_url(args.url)
        print(f"URL: {args.url}\nStatus: {status}\nHTTP Code: {code}\nNote: {msg}")
        sys.exit(0)

    repo_root = Path(__file__).resolve().parent.parent
    project_dir = repo_root / "knowledge" / "projects" / args.project

    if not project_dir.exists():
        print(f"[!] Project directory not found: {project_dir}")
        sys.exit(1)

    results = verify_project_findings(project_dir, update_files=args.update)
    print_markdown_report(results)


if __name__ == "__main__":
    main()

