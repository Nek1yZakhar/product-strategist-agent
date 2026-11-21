# TICKET-15: Скриншоты реальной сессии в конкурсном PDF

> **Статус**: PLANNED (волна 2, спринт-аудит 2026-11-22)
> **Приоритет**: P1 — регламент прямо требует «Описание работы — PDF или документ по ссылке, **со скриншотами**». Текущий PDF (`docs/MGIMO_AI_Challenge_Megafon_Strategist.pdf`, 5 страниц) — только текст.

## 1. Контекст, проблема и инварианты (Context, Problem & Invariants)

### 1.1. Контекст и бизнес-проблема
PDF-пакет генерируется скриптом `scripts/generate_submission_pdf.py` (weasyprint, HTML → A4). Скриншоты в документе отсутствуют. Жюри ожидает визуальные доказательства работы агента: скриншоты — обязательный элемент регламента. Источник скриншотов — реальный прогон TICKET-13 (никаких постановочных кадров).

### 1.2. Архитектурные инварианты
- **Real-Screenshots-Only Invariant**: каждый PNG снят из живой сессии TICKET-13 или реального вывода CLI-скриптов. Запрещены макеты и коллажи «как могло бы выглядеть».
- **Numbered-Artifact Invariant**: файлы лежат в `docs/screenshots/` с нумерацией, соответствующей порядку в PDF; имена — на английском.
- **Readable-In-PDF Invariant**: ширина изображений в PDF ≥ 140 мм, текст на скриншоте должен быть читаем при печати A4 (масштаб интерфейса при записи 125–150%).
- **Dependency**: выполняется после TICKET-13 (нужен материал для съёмки).

---

## 2. Список скриншотов (обязательный набор)

| № | Файл | Что на кадре | Откуда берётся |
| :-: | :--- | :--- | :--- |
| 1 | `docs/screenshots/01-repo-structure.png` | Дерево репозитория в IDE + открытый AGENTS.md | AntiGravity, обозреватель файлов |
| 2 | `docs/screenshots/02-intake-dialogue.png` | Уточняющий диалог агента (≤2 вопроса) после нечёткого запроса | Чат AntiGravity (сессия TICKET-13) |
| 3 | `docs/screenshots/03-findings-frontmatter.png` | Finding с YAML-шапкой и глубокой ссылкой + результат `verify_citations.py --update` | IDE + терминал |
| 4 | `docs/screenshots/04-options-matrix.png` | Таблица 4 вариантов (Status Quo / Shutdown / Heavy Portal / Lightweight Core) | `options.md` в предпросмотре |
| 5 | `docs/screenshots/05-adversarial-review.png` | Фрагмент red-team аудита GLM 5.3 (вердикт + уязвимость) | `adversarial-review.md` |
| 6 | `docs/screenshots/06-strategy-fragment.png` | Ключевой раздел продуктовой стратегии (инварианты, экономика 285 млн ₽) | `product-strategy.md` |
| 7 | `docs/screenshots/07-resume-new-chat.png` | Новый чат: агент восстанавливает состояние из `STATE-current-task.md` | Чат AntiGravity (сцена паузы/резюме) |
| 8 | `docs/screenshots/08-cost-summary.png` | Вывод `python scripts/cost_summary.py` (таблица токенов/затрат) | Терминал |

---

## 3. Контракты реализации (Implementation Contracts)

### 3.1. Встраивание в PDF
В `scripts/generate_submission_pdf.py` (HTML_CONTENT):
- Подготовить PNG (обрезка лишних полей, ширина ≥ 1600 px, PNG-24).
- Вставить секцию «Приложение: доказательства работы агента» перед 40-балльной матрицей: каждое изображение — `<figure><img src="docs/screenshots/NN-....png" style="width:100%"/><figcaption>Рис. N — описание</figcaption></figure>`.
- `base_url=repo_root` уже задан в скрипте — относительные пути в `src` работают без изменений логики.
- Добавить в текстовые секции перекрёстные ссылки на рисунки («см. Рис. 3»).

### 3.2. Регенерация и проверка
```bash
pip install -r requirements-pdf.txt   # из TICKET-14
python scripts/generate_submission_pdf.py
# Проверка: страниц 7–9, каждое изображение открывается в PDF-просмотрщике, размер файла ≤ 15 МБ
```

### 3.3. Связанные обновления
- `docs/SUBMISSION.md`: строка «PDF-описание проекта» — статус «ГОТОВО (со скриншотами)».
- `docs/specs/TRACEABILITY.md`: чек-лист материалов — ссылка на обновлённый PDF.

---

## 4. Чеклист приемки (Forensic Acceptance Checklist)

- [ ] В `docs/screenshots/` лежат 8 PNG из таблицы раздела 2, все из реальной сессии/выводов.
- [ ] PDF перегенерирован: 7–9 страниц, рисунки читаемы в печати A4, подписи «Рис. N — …» на месте.
- [ ] Ни один скриншот не является макетом или постановкой.
- [ ] `docs/SUBMISSION.md` и TRACEABILITY отражают новый статус PDF.
- [ ] Итоговый PDF закоммичен в `docs/MGIMO_AI_Challenge_Megafon_Strategist.pdf` (замена старой версии).
