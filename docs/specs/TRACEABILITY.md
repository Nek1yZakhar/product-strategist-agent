# Матрица трассируемости требований (TRACEABILITY MATRIX)

**Конкурс**: MGIMO AI Challenge 2026  
**Номинация**: «ИИ-проект»  
**Трек**: «Стратег Фабрики продуктов МегаФона»  
**Автор**: **Захар (Solo Maker)**  

Этот документ устанавливает 100% двустороннюю связь между официальными требованиями конкурса и разработанными инженерными тикетами, навыками и файловыми артефактами репозитория.

---

## 1. Обязательный минимум требований (Core Requirements)

| № | Требование конкурсного задания | Реализующий тикет | Навык или CLI-скрипт | Проверяемый артефакт в репозитории |
| :-: | :--- | :--- | :--- | :--- |
| **1** | **Постановка задачи**<br/>Уточнение цели, адресата, контекста, ограничений и данных. Задавать только то, что влияет на шаг ($\le 2$ вопросов). | `TICKET-03`<br/>`TICKET-05` | `skill:strategist` | `knowledge/projects/demo-megafon/brief.md`<br/>`state/STATE-current-task.md` |
| **2** | **Сбор материалов**<br/>Сбор из открытых источников; каждое фактологическое утверждение обязано содержать прямую ссылку на источник. | `TICKET-04`<br/>`TICKET-07` | `skill:evidence-collector`<br/>`scripts/verify_citations.py` | `knowledge/projects/demo-megafon/findings/*.md`<br/>(5 файлов с YAML-шапкой) |
| **3** | **Проблемное исследование**<br/>План строится от вопросов для принятия решений; триангуляция источников; честное указание лакун. | `TICKET-02`<br/>`TICKET-03` | `skill:research-planner` | `knowledge/methodology/evidence-standards.md`<br/>Разделы триангуляции в `findings/` |
| **4** | **Формирование вариантов**<br/>$\ge 3$ различных вариантов, ОБЯЗАТЕЛЬНО включая «Оставить как есть» и «Закрыть направление»; контраргументы к каждому. | `TICKET-03`<br/>`TICKET-05` | `skill:options-generator`<br/>`skill:adversarial-reviewer` | `knowledge/projects/demo-megafon/output/options.md`<br/>`output/adversarial-review.md` |
| **5a**| **Продуктовая стратегия**<br/>Аудитория и JTBD, альтернативы, выбранный вектор и осознанные отказы, связь ценности с себестоимостью. | `TICKET-03`<br/>`TICKET-05` | `skill:strategy-writer` | `knowledge/projects/demo-megafon/output/product-strategy.md` |
| **5b**| **Коммуникационная стратегия**<br/>Аудитория и ситуация контакта, барьеры, ключевое сообщение и RTB, роли каналов, честность обещаний. | `TICKET-03`<br/>`TICKET-05` | `skill:strategy-writer` | `knowledge/projects/demo-megafon/output/communication-strategy.md` |
| **5c**| **План валидации**<br/>Ожидаемое изменение метрик, база для сравнения (baseline), окно наблюдения, мониторинг каннибализации. | `TICKET-03`<br/>`TICKET-05` | `skill:strategy-writer` | `knowledge/projects/demo-megafon/output/validation-plan.md` |
| **6** | **Человеческий контроль (Human-in-the-loop)**<br/>Пошаговый сценарий с контрольными точками выбора человеком на ключевых развилках. | `TICKET-01`<br/>`TICKET-03` | `.agents/rules/workflow.md`<br/>`skill:strategist` | Чекпоинты в `demo/RUNBOOK.md` и диалогах |
| **7** | **4-слойная изоляция знаний**<br/>Раздельное хранение: инструкции / методология / материалы проекта / текущее состояние задачи. | `TICKET-01`<br/>`TICKET-02` | `.agents/rules/knowledge.md` | Каталоги `.agents/`, `knowledge/`, `state/` |
| **8** | **Возобновляемость работы**<br/>Продолжение работы после паузы, включая открытие НОВОГО окна чата (файловый стейт в стиле Manus). | `TICKET-06` | `skill:session-resume` | `state/STATE-current-task.md`<br/>`state/decision-journal.md` |
| **9** | **Прозрачность и учет затрат**<br/>Прозрачность действий, оснований и стоимости (учет токенов и расчет расходов по каждому шагу). | `TICKET-04`<br/>`TICKET-09` | `scripts/cost_summary.py`<br/>`.agents/rules/cost.md` | `state/cost-log.csv`<br/>Табличный финансовый отчет |

---

## 2. Дополнительный (бонусный) уровень требований

| Бонусная возможность | Архитектурная и методологическая реализация | Тикет | Проверяемый артефакт |
| :--- | :--- | :---: | :--- |
| **Интервью и синтетические персоны** | LLM-персоны строго маркируются как генерация гипотез и НЕ являются подтверждением спроса (arXiv:2607.26348). | `TICKET-08` | `knowledge/methodology/synthetic-respondents.md`<br/>`skill:interview-panel` |
| **Защита от галлюцинаций ссылок** | Детерминированная проверка сетевых ссылок скриптом по протоколам HEAD/GET (arXiv:2504.00317, arXiv:2607.00738). | `TICKET-04`<br/>`TICKET-07` | `scripts/verify_citations.py`<br/>Таблица аудита (100% verified) |
| **UX-анализ интерфейсов** | Анализ реального пользовательского пути и устранение отвала 42% на SMS-онбординге. | `TICKET-05` | `knowledge/projects/demo-megafon/output/ux-journey.md` |
| **Воспроизводимый анализ данных** | Расчеты на чистом Python: базовые метрики, LTV-якорь удержания (+500 ₽/мес валовой прибыли). | `TICKET-04`<br/>`TICKET-05` | `knowledge/projects/demo-megafon/data/baseline-metrics.md` |
| **Поддержка принятия решений** | Протоколирование решений в журнале с владельцами, метриками и условиями пересмотра. | `TICKET-03`<br/>`TICKET-05` | `state/decision-journal.md`<br/>(Запись `DEC-2026-MF-01`) |
| **Актуализация при новых данных** | Автоматическое отслеживание затронутых выводов стратегии при поступлении свежих рыночных вводных. | `TICKET-03` | `skill:revision-scanner`<br/>`.agents/rules/knowledge.md` |
| **Маршрутизация и Red-Team** | Основной стратег в AntiGravity (Gemini Flash), независимый Red-Team критик в Zcode (GLM 5.3), копайлот Perplexity. | `TICKET-09` | `docs/ARCHITECTURE.md`<br/>`output/adversarial-review.md` |
| **Сценарный движок видео** | Посекундный план 10-минутного ролика и эталонный лог сессии для терминальных реплеев. | `TICKET-10` | `demo/VIDEO-PLAN.md`<br/>`demo/session_transcript.jsonl` |
| **Портативность без фреймворков** | Чистый репозиторный агент без демонов, совместимый с AntiGravity, Cursor, Claude Code, Zcode. | `TICKET-01`<br/>`TICKET-11` | `AGENTS.md`<br/>`README.md` |

---

## 3. Чек-лист обязательных материалов сдачи

| Конкурсный материал | Формат и требования | Статус готовности | Файл в репозитории |
| :--- | :--- | :---: | :--- |
| **1. Репозиторий Git** | Публичный или приватный репозиторий с инструкцией запуска за 5 минут. | **ГОТОВО** | [README.md](file:///c:/Users/Admin/Desktop/product-strategist-agent/README.md) |
| **2. Демо-кейс МегаФона** | Сквозной кейс по семейной связи на открытых данных. | **ГОТОВО** | `knowledge/projects/demo-megafon/` |
| **3. Видеозапись ($\le 10$ мин)** | Запрос $\to$ работа агента $\to$ варианты $\to$ стратегия $\to$ возобновление. | **ГОТОВО** | `demo/VIDEO-PLAN.md`, `demo/RUNBOOK.md` |
| **4. PDF-описание проекта** | Архитектура, реестр моделей, промпты, бонусы, бюджет, ограничения. | **ГОТОВО** | `docs/CONTEXT.md`, `docs/ARCHITECTURE.md` |
