# TICKET-14: Гигиена репозитория и переносимость (Repo Hygiene & Portability)

> **Статус**: PLANNED (волна 2, спринт-аудит 2026-11-22)
> **Приоритет**: P1 — жюри открывает репозиторий на GitHub; битые ссылки и падающие команды quickstart бьют по критерию «Имплементация».

## 1. Контекст, проблема и инварианты (Context, Problem & Invariants)

### 1.1. Контекст и бизнес-проблема
Аудит зафиксировал дефекты переносимости, оставшиеся от локальной разработки на Windows:
1. **14 абсолютных ссылок `file:///c:/Users/Admin/Desktop/product-strategist-agent/...`**: 13 в `docs/STATE.md` (реестр тикетов + ссылка на TRACEABILITY), 1 в `docs/specs/TRACEABILITY.md`. На GitHub эти ссылки мёртвые.
2. **README quickstep ссылается на несуществующий файл**: строка 52 — `python scripts/extract_brief.py Primer-brifa.pdf --project demo-megafon`, при том что бриф в корне называется `Пример брифа.pdf`. Команда падает у любого, кто повторяет инструкцию. Дефолт скрипта (`scripts/extract_brief.py`, строка 121: `default="Primer-brifa.pdf"`) содержит ту же ошибку.
3. **LICENSE отсутствует**, хотя README несёт бейдж MIT.
4. **Противоречие зависимостей**: README заявляет «только стандартная библиотека», но `scripts/generate_submission_pdf.py` импортирует `weasyprint`. Регенерация PDF без инструкции по зависимостям невозможна.
5. **Фантомный артефакт**: `docs/specs/TRACEABILITY.md` ссылается на `state/citation-report.md`, которого нет в репозитории (скрипт печатает отчёт в stdout, но не сохраняет файл).

### 1.2. Архитектурные инварианты
- **Relative Link Invariant**: в Markdown-документации допустимы только относительные пути внутри репо и абсолютные URL в интернете. Локальные абсолютные пути запрещены.
- **Quickstart-Must-Run Invariant**: каждая команда из README выполняется на чистом клоне без правок.
- **License-Truth Invariant**: заявленный бейдж лицензии подкреплён файлом LICENSE.
- **Dependency-Truth Invariant**: все внешние зависимости перечислены явно, stdlib-заявления соответствуют действительности.

---

## 2. Контракты реализации (Implementation Contracts)

### 2.1. Замена битых ссылок
```bash
# Все вхождения (ожидается 0 после фикса; спеки и аудит-отчёт исключены —
# они упоминают паттерн как документирование дефекта, а не как ссылки):
grep -rn "file:///c:/" docs/ README.md --exclude-dir=specs --exclude=AUDIT-2026-11-22.md
```
- `docs/STATE.md`: в 11 строках таблицы реестра заменить `file:///c:/Users/Admin/Desktop/product-strategist-agent/<path>` на относительный путь `../<path>` (таблица лежит в `docs/`, пути ведут в корень репо); ссылку на TRACEABILITY — на `specs/TRACEABILITY.md`; в журнальной записи — на относительные пути.
- `docs/specs/TRACEABILITY.md`: ссылку на README — на `../../README.md`.

### 2.2. Починка quickstart
- `README.md:52`: `python scripts/extract_brief.py "Пример брифа.pdf" --project demo-megafon` (кавычки обязательны — пробел и кириллица в имени файла).
- `scripts/extract_brief.py:121`: `default="Пример брифа.pdf"` + обработка отсутствия файла с понятным сообщением (см. `sasha`-стандарт сообщений).
- Дополнительно: если в окружении пользователя нет кириллического имени, добавить fallback на поиск `*.pdf` в корне с подсказкой.

### 2.3. Лицензия
- Создать `LICENSE` (MIT, copyright 2026 Zakhar). Текст — канонический с `https://opensource.org/license/mit`.

### 2.4. Зависимости PDF-генератора
- Создать `requirements-pdf.txt`: `weasyprint>=61` (одна строка, закомментированное назначение).
- В README секцию «Требования» дополнить: «Для регенерации PDF-описания дополнительно: `pip install -r requirements-pdf.txt`». Формулировку «сторонние зависимости не требуются» уточнить: «для CLI-инструментов анализа — только stdlib; для регенерации PDF — weasyprint».

### 2.5. Фантомный артефакт
- Выполнить `python scripts/verify_citations.py --project demo-megafon --update` (создаёт `state/citation-report.md`) и закоммитить отчёт. Если флаг `--update` не пишет файл — расширить скрипт записью отчёта в `state/citation-report.md` (контракт схемы уже описан в TICKET-07, раздел 3.2).

---

## 3. Чеклист приемки (Forensic Acceptance Checklist)

```bash
# 1. Битых локальных ссылок нет (спеки/аудит исключены как документирование)
! grep -rn "file:///c:/" docs/ README.md --exclude-dir=specs --exclude=AUDIT-2026-11-22.md && echo "relative-links: OK"

# 2. Quickstart-команды выполняются на чистом клоне
python scripts/extract_brief.py "Пример брифа.pdf" --project demo-megafon
python scripts/teamwork_runner.py --validate-all
python scripts/cost_summary.py > /dev/null && echo "cost_summary: OK"

# 3. LICENSE на месте
test -f LICENSE && echo "license: OK"

# 4. citation-report существует
test -f state/citation-report.md && echo "citation-report: OK"

# 5. PDF-зависимости задокументированы
grep -q weasyprint requirements-pdf.txt && echo "pdf-deps: OK"
```

- [ ] `grep -rn "file:///c:/" docs/ README.md --exclude-dir=specs --exclude=AUDIT-2026-11-22.md` возвращает пусто.
- [ ] Команда из README с `Пример брифа.pdf` проходит без правок.
- [ ] LICENSE закоммичен; бейджу MIT соответствует файл.
- [ ] `state/citation-report.md` в репозитории; TRACEABILITY ссылается на существующий файл.
- [ ] README не содержит ложных заявлений о зависимостях.
