# Strategic Decision Journal

This journal records formal product and communication decisions, their rationale, assigned owners, tracking metrics, and explicit revision triggers.
Compliant with Solo-Maker Architecture & Zero Corporate Theater (Rule 2).

---

## Log Schema

| Field | Description |
| :--- | :--- |
| **Decision ID** | Unique identifier (e.g., `DEC-2026-MF-01`) |
| **Timestamp** | ISO-8601 UTC timestamp |
| **Project** | Target project (`demo-megafon`) |
| **Options Weighed** | List of evaluated options (incl. Status Quo and Shutdown) |
| **Selected Option** | Winning strategic direction |
| **Core Rationale** | Key justification linking user value to unit economics |
| **Accepted Counterarguments** | Legitimate risks identified by red-team and how they are mitigated |
| **Owner** | Responsible manager (Захар, Solo Maker) |
| **Primary Metric** | Key KPI & target threshold |
| **Revision Trigger** | Condition that mandates reopening the decision |

---

## Decision Records

### [DEC-2026-MF-01] Утверждение продуктовой стратегии «МегаФон Семья: Забота и упреждающий сигнал»
- **Timestamp**: `2026-11-22T04:25:00Z`
- **Project**: `demo-megafon` (MGIMO AI Challenge 2026 / Фабрика продуктов МегаФона)
- **Options Weighed**:
  1. *Вариант А (Выбран)*: «Упреждающий сигнал и быстрый шеринг в текущем приложении» (Lightweight Core, 3.0 чел.-мес. разработки в Q2, цель 285 млн ₽ валовой прибыли, 12 000 доп. месяцев).
  2. *Вариант B (Отклонен)*: «Полномасштабный семейный хаб с ролевой моделью» (Heavy Portal, 5.5+ чел.-мес., гарантированный срыв сроков пилота Q2).
  3. *Вариант C (Отклонен)*: «Status Quo / Без изменений» (Инерционная траектория 279 млн ₽, недобор 6 млн ₽, стагнация на 5 000 групп).
  4. *Вариант D (Отклонен)*: «Shutdown / Закрытие направления» (Остановка сервиса, высвобождение ресурсов, риск цепного оттока домохозяйств).
- **Selected Option**: **Вариант А («Упреждающий сигнал и быстрый шеринг в текущем приложении»)**
- **Core Rationale**:
  - Устраняет ключевую боль клиента (перебои интернета и панику) за 45 минут до отключения без когнитивной перегрузки.
  - Строго укладывается в норматив трудозатрат: 3.0 человеко-месяца разработки backend/mobile и 1.0 человеко-месяц QA во втором квартале.
  - Детерминированная юнит-экономика: выход на 12 000 дополнительных оплаченных месяцев удержания по 500 ₽ валовой прибыли генерирует ровно $+6\,000\,000$ ₽, обеспечивая достижение годовой планки в **285 млн ₽** при **8 000 активных** и **12 000 подключенных группах**.
  - Полная окупаемость инвестиций (2.8 млн ₽) в середине Q4 планового года.
- **Accepted Counterarguments & Mitigations (GLM 5.3 Red-Team Audit)**:
  1. *Риск спам-пушей*: Ограничение до 1 пуш-предупреждения на событие, настраиваемый порог детекции (10% квоты).
  2. *Расползание скоупа разработки*: Жесткий мораторий на кастомные экраны в пилоте Q2; опора на существующую шину событий и нативные пуши с 1 кнопкой шеринга.
  3. *Тайна связи и 152-ФЗ*: Изолированные согласия — шеринг остатка трафика строго отделен от согласия на просмотр начислений. Мгновенная деактивация при отзыве согласия.
- **Owner**: **Захар (Solo Maker)**
- **Primary Metric**: Валовая прибыль $\ge 285$ млн ₽, 8 000 активных / 12 000 подключенных групп, доля активаций за 14 дней $\ge 60\%$, снижение перебоев с 12% до 9%.
- **Revision Triggers (Критерии пересмотра)**:
  - Доля блокировок интернета по итогам 6 недель пилота в Q2 не снизилась ниже 11.2%.
  - Зафиксирован хотя бы один факт утечки приватности (отображение данных после отзыва согласия).
  - Зафиксированы повторные списания средств или двойной вычет пакета трафика.
  - Дефицит разработки в Q2 превышает 5 рабочих дней без возможности компенсации.
