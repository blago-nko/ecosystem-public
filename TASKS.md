# 📋 TASKS.md — Реестр задач и артефактов экосистемы `blago-nko`

> Краткосрочные задачи — ниже. Протокол ведения задач: [AGENTS.md](AGENTS.md) §5. Живые метрики: [docs/STATUS.md](docs/STATUS.md). Долгосрочные направления (P2) — в [ROADMAP.md](ROADMAP.md). **Тип документа:** живой реестр. Единый источник правды по **активным работам** и **состоянию артефактов** (скрипты / конфиги / workflows / компоненты).
> **Триггер обновления:** каждый закрытый протокол (смерженный PR) → немедленное обновление.
> **Исполнитель:** 🤖 ИИ-агент (бесплатные инструменты, доступные в РФ без VPN) → 👤 подтверждение Основателя.
> **Сроки:** не фиксируются (решение Основателя). Управление через **Фазы** и **Приоритеты**.
> **Иерархия:** документ подчинён САМ. Префиксы протоколов — по САМ п. 1.5 (`SAM-`, `CAN-`, `GP-`, `SUMKA-`, `MIG-`, `LIC-`, `INFRA-`, `VAC-`).

---

## Текущее состояние (As-Is, снимок после регистрации научного домена 09.11.2026)

| Параметр | Состояние |
| :--- | :--- |
| НКО | ✅ Официально зарегистрирована |
| 13 сайтов на Hugo | 🟢 Функционируют на Blogger |
| Пантеон | 🟢 Функционирует на Blogger, ~350 страниц (цель 16 505) |
| САН | 🟢 Функционирует на Blogger |
| gallery | ❌ Удалён из активной архитектуры (DR-MEDIA M1); link-remediation — MEDIA-001 |
| Science (Vacuum Condensate) | 🟡 Зарегистрирован в графе, репо создан, ожидает наполнения |
| Контент | ✅ Жив на Blogger — подлежит перепарсиванию |
| `shared-assets` | ❌ Удалён при сбросе 11.09.2026, пересоздаётся (задача INFRA-010) |
| `can-secure-dev` | ❌ Org отменена (DR-SAN S1); контур B — логический в монорепе (DR-SAN S2) |
| Домены / DNS | ✅ Зарегистрированы, ведут на старые сайты (Blogger); science.obrazslov.ru готов к CNAME |
| Secrets | ⚠️ Не проверены после сброса |

**Модель развития:** постоянно развивающаяся экосистема. НКО зарегистрирована, сайты функционируют на Blogger, выполняется поэтапная реализация манифестов и запуск новых Greenfield-проектов.

## Легенда

**Статусы:** ⬜ Не начата · 🔄 В работе · ✅ Завершена · ⛔ Заблокирована
**Приоритеты:** 🔴 Критический · 🟠 Высокий · 🟡 Средний · 🟢 Низкий
**Фазы:** `0 Фундамент` → `1 Каркас` → `2 Наполнение/Миграция`
**Имя определено:** ✅ Да (можно сразу создавать/проверять) · ❌ Нет (концепт, требуется проектирование)

---

---

## Canonical Decision Records

> Решения основателей, на которые ссылаются протоколы. Утверждены 2026-11-28. Префиксы задач реализации: `MEDIA-` (временный operational-префикс до утверждения в САМ §1.5, по аналогии с `REG-`, задача REG-009) и `CAN-` серия 101+ (зарезервирована под DR-SAN).

### DR-MEDIA — Галерея и изображения

| ID | Решение | Описание |
| :--- | :--- | :--- |
| **M1** | Удаление gallery.obrazslov.ru | Тестовый Blogger-фотоархив удаляется из активной архитектуры (remove_from_active_architecture_and_delete_site). Отдельный публичный «ФОТОАРХИВ НКО» не требуется. |
| **M2** | Preserve Blogger URLs | Старые изображения мигрирующих сайтов остаются по ИСХОДНЫМ Blogger URL самих сайтов (не gallery). preserve — переходная мера: исходный Blogger-сайт нельзя отключать, пока на него ссылается активный мигрированный контент; перед отключением — перенос в R2 + перепись ссылок (Link Preservation до Asset Consolidation). |
| **M3** | R2-only для новых изображений | Все НОВЫЕ изображения всех контуров (Hugo/Astro/Next/САН/Пантеон/Наука/будущие) — только Cloudflare R2. Публичный медиа-домен: cdn.obrazslov.ru. Новые загрузки в Blogger запрещены. |
| **M4** | Форматы/размеры | WebP обязательный, AVIF — canonical_for в storage_policy; сетка 400/800/1200/1600, max 1600px; EXIF-strip. Точные числа подтверждаются аудитом, финализация в MIG-017 / media-pipeline протоколе. |
| **M5** | Схема путей R2 | `/media/{site-key}/{page-slug}/{image-basename}-{width}.webp` — финализация в MIG-017. |
| **M6** | Метаданные | Минимум: alt, title, license, source, author, consent, original_url; расширенный набор (site_key, page_slug, image_id, widths, formats, hash, pii_redacted, ai_safe, cdn_path, r2_key) — во front matter/asset-config + sidecar JSON/R2 object metadata; финализация в MIG-017. |
| **M7** | Link-remediation | Перед фактическим удалением домена — найти и убрать/заменить ВСЕ активные ссылки вида https://gallery.obrazslov.ru/... (контент, шаблоны, примеры JSON-LD, hotlink-схемы), чтобы не оставить 404 и чтобы агенты не продолжали использовать удалённый домен как канон. |

### DR-SAN — Отказ от can-secure-dev, ПДн в монорепе, ИИ-аккаунт

| ID | Решение | Описание |
| :--- | :--- | :--- |
| **S1** | Отмена can-secure-dev | Отдельная GitHub-организация/аккаунт can-secure-dev ОТМЕНЕНА. Не создаётся; все ссылки в нормативке и реестрах переводятся на монорепу blago-nko/ecosystem-public. |
| **S2** | Логический контур B | Контур B остаётся как ЛОГИЧЕСКИЙ/deployment-контур ПДн внутри монорепы, а не как отдельный GitHub org: repository: blago-nko/ecosystem-public + logical_contour: B + deployment_environment + pii_boundary: rf_gateway + pii_in_git: forbidden. |
| **S3** | Этап 1 (Hugo) | can.blagorussia.ru — статический Hugo-сайт в монорепе (GitHub Pages). Hugo ПДн не хранит и не обрабатывает; первичный сбор ПДн — через Яндекс (Yandex Forms / approved Yandex endpoint). ПДн в Git запрещены; допустимы только ссылки на формы, политики согласия, synthetic-примеры, конфигурация без PII. |
| **S4** | Этап 2+ (динамический) | Next.js + Vercel + Supabase ОСТАЮТСЯ в плане, но внутри монорепы (напр. apps/san/), деплой через защищённые GitHub Environments; Supabase принимает только зашифрованные payload / non-PII derived data через RF gateway (Yandex Cloud Functions — уточняется аудитом по crypto_policy.yaml); Vercel — только UI/SSR, без хранения ПДн. |
| **S5** | Изоляция ПДн без отдельного org | Компенсируется: no PII in Git; no plaintext PII в issues/PR/logs/fixtures/tests/examples; GitHub Environments + protected secrets; branch protection; CODEOWNERS/review policy для чувствительных путей; RF gateway/Yandex-граница сбора; encrypted-storage only; audit trail привилегий. |
| **S6** | ИИ-аккаунт | Отдельный аккаунт Основателя с ALTERNATE EMAIL (человеческий founder-контролируемый). Полный repo admin допустим как явное risk-accepted исключение из least-privilege. Исключение НЕ отменяет: ПДн в Git запрещены; ИИ получает только non-PII/redacted данные; redaction/tokenization gate перед зарубежным ИИ-API; production secrets — через environments; действия аудируемы. |
| **S7** | Конфликт этапов | Изоляция контура B — после финальной проверки сайтов (Этап 7) по STRATEGY.md; MIG-014 с «после Этапа 6» приводится к Этапу 7 / монорепной модели. |
| **S8** | MIG-022 отменено | MIG-022 остаётся ❌ Отменено, причина уточняется: отменён прямой переход в отдельный can-secure-dev; вместо него — монорепная поэтапная модель (Hugo этап 1 → dynamic этап 2+ в той же монорепе). |

---

## DR-MEDIA Tasks (галерея и изображения)

Удаление gallery.obrazslov.ru и переход на R2-only модель хранения. Префикс: `MEDIA-` (временный operational, см. примечание выше).

| ID | Задача | Подзадачи | Приор. | Ответств. | Статус | Комментарий |
| :--- | :--- | :--- | :---: | :--- | :---: | :--- |
| **MEDIA-001** | Link-remediation gallery.obrazslov.ru | Найти и удалить/заменить ВСЕ ссылки на gallery.obrazslov.ru в манифестах, шаблонах, JSON-LD, hotlink-схемах | 🔴 | 🤖→👤 | ⬜ | DR-MEDIA M7 |
| **MEDIA-002** | storage_policy.yaml: схема путей и метаданные | Добавить path scheme M5, metadata schema M6, width grid M4; сверить запрет новых загрузок в Blogger | 🔴 | 🤖→👤 | ⬜ | DR-MEDIA M3–M6 |
| **MEDIA-003** | domains-graph.yaml: узел gallery | Перевести узел gallery в deprecated/remove, убрать из активных связей | 🟠 | 🤖→👤 | ⬜ | DR-MEDIA M1 |
| **MEDIA-004** | MIG-017 / media-pipeline протокол | Финализация форматов, сетки размеров и путей R2 в протоколе media-pipeline | 🟠 | 🤖→👤 | ⬜ | DR-MEDIA M4–M6 |
| **MEDIA-005** | shared-assets: image_storage_routing.json | Маршрутизация: Blogger только preserve легаси (M2), новые — R2 (M3) | 🟠 | 🤖→👤 | ⬜ | DR-MEDIA M2, M3 |

---

## DR-SAN Tasks (монорепная модель САН)

Отмена can-secure-dev, контур B как логический контур монорепы. Префикс: `CAN-` серия 101+.

| ID | Задача | Подзадачи | Приор. | Ответств. | Статус | Комментарий |
| :--- | :--- | :--- | :---: | :--- | :---: | :--- |
| **CAN-101** | САН.md: убрать can-secure-dev | Переписать раздел 19 и все упоминания: монорепа + logical_contour B | 🔴 | 🤖→👤 | ⬜ | DR-SAN S1, S2, S4 |
| **CAN-102** | МИГРАЦИЯ.md: Контур Б и Progressive Contour Separation | Переписать под логический контур; изоляция после Этапа 7 | 🔴 | 🤖→👤 | ⬜ | DR-SAN S1, S2, S7 |
| **CAN-103** | TASKS.md: MIG-014 и связанные строки | Монорепная модель (apps/san/, GitHub Environments), Этап 7 | 🟠 | 🤖→👤 | ⬜ | DR-SAN S4, S7 |
| **CAN-104** | САН.md: схема ПДн-изоляции без отдельной org | Environments, secrets, CODEOWNERS, RF gateway, audit trail | 🟠 | 🤖→👤 | ⬜ | DR-SAN S3, S5 |
| **CAN-105** | AGENTS.md: политика ИИ-аккаунта | ALTERNATE EMAIL, risk-accepted full admin, redaction gate | 🟠 | 🤖→👤 | ⬜ | DR-SAN S6 |
| **CAN-106** | Реестры: contour B в domains-graph/identity | logical_contour: B, pii_boundary: rf_gateway | 🟡 | 🤖→👤 | ⬜ | DR-SAN S2 |

---

## ФАЗА 0 — РЕГИСТРАЦИЯ НАУЧНОГО ДОМЕНА (Завершено)

| ID | Задача | Подзадачи | Приор. | Ответств. | Статус | Комментарий |
| :--- | :--- | :--- | :---: | :--- | :---: | :--- |
| **VAC-001** | Создание репозитория проекта | `blago-nko/vacuum-condensate-hypothesis` | 🔴 | 👤 | ✅ | Репозиторий создан, структура Astro подготовлена |
| **VAC-002** | Разработка манифеста домена | Draft `ВАКУУМНЫЙ_КОНДЕНСАТ.md` | 🔴 | 🤖→👤 | ✅ | Манифест утвержден, позиционирование как метафизико-научный портал |
| **VAC-003** | Обновление графа доменов | Добавить узел `vacuum_condensate` в `domains-graph.yaml` | 🔴 | 🤖→👤 | ✅ | Узел добавлен, связи Hub-and-Spokes обновлены (PR #338) |
| **VAC-004** | Синхронизация README | Обновить таблицу манифестов и счетчик доменов (14→15) | 🟠 | 🤖→👤 | ✅ | Таблица обновлена, ссылка на репо добавлена |
| **VAC-005** | Лицензионное исключение | Зафиксировать CC BY 4.0 / MIT в `ЛИЦ.md` | 🔴 | 🤖→👤 | ✅ | Раздел 5 Исключения для науки добавлен в ЛИЦ.md |
| **VAC-006** | Инструкции для агентов | Правила работы с LaTeX/Python в `AGENTS.md` | 🟠 | 🤖→👤 | ✅ | Раздел 9 Специфика домена ВАКУУМНЫЙ_КОНДЕНСАТ добавлен |
| **VAC-007** | Логирование в плане миграции | Отметить как Greenfield проект в `МИГРАЦИЯ.md` | 🟡 | 🤖→👤 | ✅ | Группа В: Новые домены, пункт 15 добавлен |

---

## DOM-VACUUM Tasks (Vacuum Condensate Domain Implementation)

Научно-исследовательский портал `science.obrazslov.ru`. Префикс протокола: `VAC-`.

### Техническая реализация Astro проекта (В работе)

- [ ] VAC-008: Setup Astro project structure compatible with `shared-assets`.
  - *Описание:* Инициализация папок `src/content/articles/`, настройка `astro.config.mjs` для поддержки Markdown/MDX.
  - *Зависимость:* Требует наличия `shared-assets/css/base.css`.
- [ ] VAC-009: Configure LaTeX rendering pipeline.
  - *Описание:* Установка плагинов `remark-math` и `rehype-katex`. Проверка рендеринга формул `$E=mc^2$` на тестовой странице.
  - *Зависимость:* VAC-008.
- [ ] VAC-010: Implement first Python script for PBH mass function calculation.
  - *Описание:* Создание `scripts/pbh_calc.py` для расчета функции масс компактных узлов $dn/dM$. Генерация JSON-артефакта в `public/data/`.
  - *Зависимость:* Нет. Может выполняться параллельно с VAC-008.
- [ ] VAC-011: Port main hypothesis text to Markdown/Astro pages.
  - *Описание:* Перенос текста статьи «Гипотеза вакуумного конденсата Вселенной» в формат MDX с разбивкой на разделы (Introduction, Model, Dynamics, Black Holes, Conclusion).
  - *Зависимость:* VAC-008, VAC-009.
- [ ] VAC-012: Create interactive density evolution visualization ($\rho(a)$).
  - *Описание:* Разработка JS-компонента (Astro Island) для графика эволюции плотности энергии вселенной на основе данных из VAC-010.
  - *Зависимость:* VAC-010, VAC-011.
- [ ] VAC-013: Set up RSS feed generation `/feed.xml`.
  - *Описание:* Настройка генератора фидов для интеграции с СУМКой.
  - *Зависимость:* VAC-008.
- [ ] VAC-014: Deploy initial version to GitHub Pages under `science.obrazslov.ru`.
  - *Описание:* Настройка CI/CD workflow для публикации собранного сайта на поддомен.
  - *Зависимость:* VAC-008...013.

### Публикация и продвижение (Backlog)

- [ ] VAC-015: Prepare English abstract and key figures for international audience.
- [ ] VAC-016: Submit paper to arXiv/Zenodo with DOI linking back to this repo.
- [ ] VAC-017: Integrate social sharing buttons (VK, Telegram) via shared-assets components.

---

## ФАЗА 0 — ФУНДАМЕНТ (Legacy Infrastructure)

| ID | Задача | Подзадачи | Приор. | Ответств. | Статус | Комментарий |
| :--- | :--- | :--- | :---: | :--- | :---: | :--- |
| **LIC-001** | Решение по лицензионной модели | Зафиксировать ОДНУ модель: (а) **AGPLv3 + CC BY-NC 4.0** [рекомендуется] или (б) MIT + CC BY 4.0. Решение принимает Основатель | 🔴 | 👤 | ✅ | Закрыт PR 211: AGPLv3 (код) + CC BY-NC 4.0 (контент); детали в ЛИЦ.md |
| **LIC-002** | Синхронизация лицензий по всем файлам | Привести к единой модели: `README.md`, метаданные+тело `ЛИЦ.md`, `AGENTS.md`, `LICENSE`, `LICENSE-CONTENT` | 🔴 | 🤖→👤 | ✅ | Файлы приведены к модели; синхронизация и проверка в CI |
| **LIC-003** | Автопроверка лицензий | Контроль футера всех сайтов в `readme-license-check.yml` / `architecture-check.yml` | 🟠 | 🤖→👤 | ✅ | readme-license-check.yml активен на каждом PR |
| **PROC-002** | Роль «Хранитель графа» | Описать роль ИИ-агента в `AGENTS.md` (Протокол 016.5) | 🟠 | 🤖→👤 | ✅ | Роль описана в AGENTS.md (Протокол 016.5) |
| **INFRA-005** | Актуализация данных после сброса | Отразить реальное состояние репо/сайтов в `docs/manifests.yaml` | 🔴 | 🤖→👤 | ✅ | Данные синхронизированы sync-manifests; подтверждено VERIFY-002/003 |
| **SEC-001** | Аудит Secrets после сброса | Проверить уцелевшие секреты, скомпрометированные — ротировать | 🔴 | 👤 | ⬜ | Требует доступа Основателя |
| **ORG-001** | Верификация `can-secure-dev` | Проверить, что org пуста; подготовить к Этапу 2 САН | 🟡 | 👤 | ❌ | Отменено (DR-SAN S1): отдельная org не создаётся; контур B — логический в монорепе |
| **PROC-001** | Автовалидация `TASKS.md` | В `manifest-consistency-check.yml`: у активных задач есть статус, у закрытых — результат | 🟠 | 🤖→👤 | ✅ | check_tasks_registry.py + шаг в manifest-consistency-check.yml |
| **VERIFY-001** | Верификация существующих скриптов | Проверить 10 `.py` файлов из `/scripts/` | 🔴 | 🤖→👤 | ✅ | Статус в Реестре |
| **VERIFY-002** | Верификация существующих workflows | Проверить 13 `.yml` из `.github/workflows/` | 🔴 | 🤖→👤 | ✅ | Статус в Реестре |
| **VERIFY-003** | Верификация конфигов и шаблонов | Проверить применимость 3 `.json`, шаблона PR, конфигов линтера, `manifests.yaml`, `STATUS.md` | 🟠 | 🤖→👤 | ✅ | Статус в Реестре |

---

## ФАЗА 1 — КАРКАС

| ID | Задача | Подзадачи | Приор. | Ответств. | Статус | Комментарий |
| :--- | :--- | :--- | :---: | :--- | :---: | :--- |
| **ORG-003** | Токен для автоматизации | Получить PAT с правами создания репо + настройки Branch Protection | 🟠 | 👤 | ⬜ | Зависимость для ORG-002, INFRA-010 |
| **ORG-002** | Применение Branch Protection | Применить `branch-protection.json`, `ruleset.json` через API | 🟠 | 👤/🤖 | ⬜ | Зависит от ORG-003 |
| **INFRA-010** | Пересоздание `shared-assets` | Репозиторий общих фронтенд-артефактов | 🟠 | 🤖→👤 | ✅ | Репозиторий создан (INFRA-033); подключение через submodule |
| **INFRA-011** | Публикация в GitHub Packages | `npm.pkg.github.com`, SemVer, только через CI | 🟡 | 🤖→👤 | ⬜ | Протокол 014 САМ |
| **INFRA-012** | Reusable workflows | `architecture-check`, `protocol-check`, `sync-manifests`, `publish-assets`, `ai-rules-sync` | 🟠 | 🤖→👤 | ⬜ | Унифицировать `protocol-check`↔`pr-prefix-check` |
| **INFRA-013** | Blago Ecosystem Bot | GitHub App для кросс-орг проверок | 🟡 | 🤖→👤 | ⬜ | САМ 3.3.3 |
| **INFRA-003** | Актуализация фактов в манифестах | Пантеон: 350 стр (не 16 505); статусы сайтов | 🔴 | 🤖→👤 | ⬜ | Манифесты должны отражать реальность |
| **DOC-001** | Указатели на `TASKS.md` в манифестах | В блоках со списками артефактов вставить ссылку на «Реестр артефактов» | 🔴 | 🤖→👤 | ⬜ | Новый подход к состоянию артефактов |
| **INFRA-004** | Наполнение «Реестра артефактов» | Ревизия и заполнение таблицы ниже | 🔴 | 🤖→👤 | ⬜ | Источник правды по артефактам |
| **INFRA-015** | Аудит и очистка устаревших удалённых веток | 21 ветка удалена; оставлены main + активные авто-ветки | 🟠 | 🤖→ | ✅ | Закрыт PR (этот) |
| **INFRA-016** | Фикс MD032 в AGENTS.md (пустые строки вокруг списков) | sed-вставка пустых строк | 🟢 | 🤖→ | ✅ | Закрыт PR 192 |
| **INFRA-017** | continue-on-error для Enable Auto-Merge в sync-manifests.yml | awk-вставка флага | 🟢 | →👤 | ✅ | Закрыт PR 193 |
| **INFRA-001** | Создание domains-graph.yaml | 14 доменов, роли, контуры, связи; таксономия — INFRA-020 | 🔴 | →👤 | 🔄 | Этот PR |
| **INFRA-018** | continue-on-error для Enable Auto-Merge во всех sync-workflows | awk-вставка флага | 🟠 | 🤖→👤 | ✅ | Закрыт PR 195 |
| **INFRA-019** | Удаление update-manifest-dates.yml (осцилляция дат) | git rm воркфлоу | 🔴 | 🤖→ | ✅ | Закрыт PR 199 |
| **INFRA-020** | Наполнение таксономии domains-graph, уточнение ролей хаба и r2 | общие категории и подтаксономии по 016.2 | 🟠 | 🤖→ | ⬜ | После INFRA-001 |
| **INFRA-021** | Снятие markdownlint-долга (ГРЕК-ПАНТЕОН.md; CHANGELOG.md отсутствует) | Убраны из ignores; .markdownlintignore удалён | 🟡 | → | ✅ | Закрыт PR 220 |
| **INFRA-022** | Восстановление обязательных секций STATUS.md + генерация из источников | 4 секции из domains-graph.yaml и manifests.yaml | 🔴 | 🤖→👤 | ✅ | Этот PR |
| **INFRA-026** | Патч update_status.py: генерация 4 обязательных секций STATUS.md | из domains-graph.yaml, manifests.yaml, TASKS.md | 🔴 | 🤖→👤 | ✅ | Этот PR |
| **INFRA-024** | Удалить auto-update-status.yml (битый дубль с путём STATUS.md) | git rm | 🟠 | → | ✅ | Этот PR |
| **INFRA-028** | pull-requests: write в update-status.yml | permissions для create-pull-request | 🔴 | → | ✅ | Закрыт PR 211 |
| **INFRA-029** | Контракт единственного писателя STATUS.md | sync_manifests не пишет STATUS; update_status.py из yaml; workflow регенерирует+валидирует | 🔴 | → | ✅ | Этот PR |
| **INFRA-030** | Убрать reviewers из авто-PR; timestamp-шаг удалён (stamp владеет генератор) | фикс "Unexpected end of JSON input" и шумовых авто-PR | 🔴 | → | ✅ | Этот PR |
| **INFRA-031** | Uptime-мониторинг доменов + алерты | UptimeRobot + Telegram + runbook | 🟡 | → | ⏸️ | Отложено до миграции 13 сайтов с Blogger |
| **INFRA-032** | Бэкапы ключевых файлов + runbook восстановления | weekly-backup в ветку backups; R2 и зеркало — этап 2 | 🟡 | → | 🔄 | Этап 1: workflow + runbook |
| **INFRA-033** | Создание blago-nko/shared-assets | Hugo-тема + Astro-компоненты + CookieConsent + RSS | 🟡 | 🤖→ | ✅ | Репозиторий blago-nko/shared-assets создан |
| **INFRA-034** | CONTRIBUTING/CODE_OF_CONDUCT/SECURITY/CHANGELOG | Инфраструктура контрибьюторов + issue templates + CODEOWNERS | 🟡 | → | ✅ | Этот PR |
| **INFRA-046** | Единый .markdownlint.yaml в shared-assets | Консистентность стиля с manifests; hotfix MD013 | 🟡 | → | ✅ | Hotfix после PR 1 shared-assets |
| **INFRA-047** | Стратегия миграции 14 сайтов с Blogger на Hugo/Astro | docs/migration/STRATEGY.md; MIG-001..014; hardening E2E | 🟡 | → | ✅ | Этот PR |
| **INFRA-048** | Hardening E2E (канонический www, ретраи, 429-skip) + дизайн-решения миграции | Объединён с INFRA-047; ПДн-формы, артефакты СУМКа, apex www | 🟡 | → | ✅ | В составе INFRA-047 |
| **INFRA-049** | Проверить apex TLS/редирект blagorussia.ru | E2E попал на apex с просроченным cert; канонический www валиден; настроить apex-редирект | 🟡 | | 🔄 | Не отказ: www работает |
| **INFRA-050** | Реестр артефактов СУМКа → shared-assets | docs/migration/SUMKA-MAPPING.md; mobile-first, JSON-LD, image sanitization и др. | 🟡 | → | ✅ | Этот PR |
| **INFRA-035** | Изоляция контура B (152-ФЗ) | Логический контур B в монорепе: GitHub Environments + protected secrets + RF gateway (без отдельной org) | 🟡 | → | ⬜ | DR-SAN S2/S5/S7: после финальной проверки сайтов (Этап 7) |
| **INFRA-036** | Тесты pytest + Playwright E2E + snapshot-тесты | Unit-тесты скриптов, E2E для 14 доменов, snapshot STATUS.md | 🟡 | → | ✅ | Этот PR |
| **INFRA-037** | Правило MSYS/Python в AGENTS.md (секция 1.5) + hotfix markdown-lint | Зафиксировать эмпирическое правило + починить MD028/MD060/MD012/MD031 | 🟡 | → | ✅ | Закрыт PR 228+230 |
| **INFRA-039** | Удалить FETCH_HEAD из main + защита .gitignore | Артефакт git pull попал в репозиторий из-за сбоя force push | 🔴 | → | ✅ | Закрыт PR 232 |
| **INFRA-040** | Реструктуризация README (навигация + цифры экосистемы) | Точка входа для людей; сжатие секции автосинхронизации | 🟡 | → | ✅ | Этот PR |
| **INFRA-041** | Кросс-ссылки документов верхнего уровня + check_docs_links.py | Матрица ссылок README/AGENTS/TASKS/ROADMAP/STATUS; ссылки STATUS только через генератор | 🟡 | → | ✅ | Этот PR |
| **INFRA-042** | Правило пересоздания конфликтных авто-PR в AGENTS.md | Попытка вставки 5.5.1 — конфликт с существующей нумерацией | 🔴 | → | ❌ | Отменён |
| **INFRA-043** | Правило пересоздания конфликтных авто-PR (AGENTS.md §5.5.3) + MD060 hotfix | Правильная нумерация 5.5.3 + авто-фикс MD060 в строке 6 | 🟡 | → | ✅ | Этот PR |
| **INFRA-044** | Сверка Фазы 0 + PROC-001 (автовалидация TASKS.md) | Дедупликация LIC-001, статусы LIC-002/003/PROC-002/INFRA-005 → ✅, check_tasks_registry.py | 🟡 | → | ✅ | Закрыт PR 252 |
| **INFRA-045** | Удаление легаси корневого STATUS.md | Дубликат docs/STATUS.md; workflow работает только с docs/ | 🟡 | → | ✅ | Закрыт PR 254 |
| **INFRA-107** | Разработка `image_sanitizer.py` (Pipeline 5 этапов) | EXIF strip → WebP → Resize ≤1600px → pHash → Watermark | 🔴 BLOCKER | 🤖→ | ⬜ | Критично для Blogger безлимита |
| **INFRA-108** | Настройка Blogger Gallery (`gallery.obrazslov.ru`) | Создание блога, привязка CNAME, получение API Key | 🔴 BLOCKER | 👤 | ❌ | Отменено (DR-MEDIA M1/M3): gallery удалён из архитектуры; новые изображения — только R2 |
| **INFRA-109** | Скрипт `upload_to_blogger.py` + интеграция с API | Автоматизация загрузки sanitized-файлов | 🔴 BLOCKER | 🤖→ | ❌ | Отменено (DR-MEDIA M3): новые загрузки в Blogger запрещены; загрузка — в R2 (MEDIA-002) |
| **INFRA-110** | Конфиг `image_storage_routing.json` в shared-assets | Маршрутизация типов файлов (Blogger preserve легаси / R2 новые / Git) | 🟡 HIGH | → | ⬜ | DR-MEDIA M2/M3: единый источник правил хранения |
| **INFRA-111** | Обновление шорткода `img.html` (srcset, lazy load) | Поддержка 4 размеров, fetchpriority для Hero | 🔴 BLOCKER | 🤖→👤 | ⬜ | Core Web Vitals LCP |
| **INFRA-112** | Внедрение `design-tokens.css` и базовой типографики | CSS-переменные цветов и шрифтов PT Sans/Serif | 🟡 HIGH | →👤 | ⬜ | Единый стандарт фронтенда |
| **INFRA-113** | Реализация `CookieConsent.js` и `footer-legal.html` | Юридическое требование 152-ФЗ и ЛИЦ | 🔴 BLOCKER | 🤖→ | ⬜ | Обязательный компонент футера |
| **INFRA-114** | Внедрение `StickyBottomBar.js` в тему Hugo | Mobile-First навигация (xs:320px) | 🟡 HIGH | →👤 | ⬜ | UX-требование Манифеста |
| **INFRA-115** | Настройка Pagefind (конфиг + JS) в теме Hugo | Исправление glob для подкаталогов GH Pages | 🟡 HIGH | → | ⬜ | Внутренний поиск по сайту |
| **INFRA-116** | Разработка `generate_redirect_map.py` | Парсинг sitemap Blogger → маппинг новых slug | 🔴 BLOCKER | 🤖→ | ⬜ | SEO-преемственность |
| **INFRA-117** | Разработка `validate_redirect_map.py` | Проверка циклов, дублей, валидности URL | 🟡 HIGH | 🤖→ | ⬜ | Качество данных редиректов |
| **INFRA-118** | Настройка `robots.txt` и `ai-hints.txt` | GEO-оптимизация, разрешение для GPTBot/Yandex | 🟡 MED | 🤖→ | ⬜ | Доступность для ИИ-поисковиков |

### Фаза 3: Миграция 14 сайтов с Blogger

| ID | Задача | Описание | Приоритет | Владелец | Статус | Комментарий |
| :--- | :--- | :--- | :---: | :--- | :---: | :--- |
| **MIG-001** | Миграция <www.blagorussia.ru> (хаб) | Hugo, сложная навигация, 13 рубрик; apex → www редирект | 🟡 | → | ⬜ | Этап 3 |
| **MIG-002** | Миграция obrazslov.ru (база знаний) | Hugo, пилот на staging. Текст мигрирован, SEO/поиск/тема проверены. Перевод на боевой домен — после блока артефактов. | 🟢 | → | 🔄 | Этап 1 частично: локализация обложек/URL-маппинг в блоке артефактов. |
| **MIG-003** | Миграция partnerstvo.blagorussia.ru (юридический хаб НП) | Hugo + секция «Документы»; ПДн-формы → Yandex Forms | 🟡 | → | ⬜ | Этап 3 |
| **MIG-004** | Миграция novosti.blagorussia.ru | Hugo, новостной поток | 🟡 | → | ⬜ | Этап 3 |
| **MIG-005** | Миграция ot-gorozan.blagorussia.ru | Hugo, медиа-контент; формы без ПДн | 🟡 | → | ⬜ | Этап 3 |
| **MIG-006** | Миграция obavlenia.blagorussia.ru | Hugo, объявления | 🟡 | → | ⬜ | Этап 3 |
| **MIG-007** | Миграция interesnye-mesta.obrazslov.ru | Hugo, архив | 🟡 | → | ⬜ | Этап 3 |
| **MIG-008** | Миграция moisites.blagorussia.ru | Hugo, школа | 🟡 | → | ⬜ | Этап 3 |
| **MIG-009** | Миграция joga.blagorussia.ru | Hugo, йога | 🟡 | → | ⬜ | Этап 3 |
| **MIG-010** | Миграция ideologia.obrazslov.ru | Hugo, тексты | 🟡 | → | ⬜ | Этап 3 |
| **MIG-011** | Миграция nasa-istoria.blagorussia.ru (Наша история) | Hugo; ПДн-формы → Yandex Forms | 🟡 | → | ⬜ | Этап 3 |
| **MIG-012** | Миграция grekpanteon.obrazslov.ru | Astro, пантеон (САМ §1.3) | 🟡 | → | ⬜ | Этап 3 |
| **MIG-013** | Миграция gallery.obrazslov.ru | Blogger, фотоархив (платформа не меняется); репозиторий gallery-npo под пайплайны | 🟡 | → | ❌ | Отменено (DR-MEDIA M1): gallery удалён из активной архитектуры |
| **MIG-014** | Миграция can.blagorussia.ru (САН) | Next.js/Vercel; вместе со всеми сайтами; изоляция — после Этапа 6 | 🟡 | → | ⬜ | Этап 3 |

---

## ФАЗА 2 — НАПОЛНЕНИЕ / МИГРАЦИЯ

| ID | Задача | Подзадачи | Приор. | Ответств. | Статус | Комментарий |
| :--- | :--- | :--- | :---: | :--- | :---: | :--- |
| **MIG-015** | Спасение контента 11 RSS | Перепарсинг живых Blogger-сайтов, бэкап в R2/YOS (0 ₽) | 🟠 | 🤖→👤 | ⬜ | Пока контент жив |
| **MIG-016** | Спасение контента Пантеона | Перепарсинг ~350 страниц + синхронизация с Google Таблицей | 🟠 | 🤖→👤 | ⬜ | Источник — живая Таблица |
| **MIG-017** | Image Sanitization Pipeline | 5 этапов: скачивание оригинала (снятие размерного суффикса Blogger URL), EXIF-очистка, WebP, 4 размера 400–1600px, ресайз ≤1600px для безлимита Blogger | 🟠 | 🤖→👤 | ⬜ | Централизованный компонент |
| **MIG-018** | Оформление gallery | Контент, `ImageGallery`, `FAQPage`, блок «Раскрытие интересов» | 🟡 | 🤖→👤 | ❌ | Отменено (DR-MEDIA M1): gallery удалён из активной архитектуры |
| **MIG-019** | Миграция 11 RSS на Hugo | Парсинг → Hugo → GitHub Pages → DNS → 301 | 🟡 | 🤖→👤 | ⬜ | После Фазы 1 |
| **MIG-020** | Пантеон: Этап 1 → Этап 2 | Статический дамп (Hugo) → Astro + YOS/DuckDB | 🟡 | 🤖→👤 | ⬜ | 350 → 16 505 страниц поэтапно |
| **MIG-022** | САН: витрина → Next.js | Статическая заглушка (без ПДн) → монорепа apps/san/ (Vercel/Supabase через Environments) | 🟢 | 🤖→👤 | ❌ | Отменено (DR-SAN S8): прямой переход в отдельный can-secure-dev отменён; монорепная поэтапная модель (Hugo этап 1 → dynamic этап 2+), см. STRATEGY.md |
| **UIX-001** | Интерактив: стратегия деградации | Этап 1: комментарии в архиве, формы через Formspree; Этап 2+: анонимизация ПДн | 🟡 | 🤖→👤 | ⬜ | 152-ФЗ |

---

## 🗂️ Реестр артефактов (источник правды)

> Манифесты ссылаются на этот раздел. Один артефакт = одна строка.

### Блок А: Существует в репо `blago-nko/manifests` (33 файла)

Все файлы физически существуют, но **не тестировались** после «Эпохального сброса».

| Путь | Манифест | Статус | Задача | Имя определено |
| :--- | :--- | :---: | :--- | :---: |
| `scripts/apply_arch_patches.py` | AGENTS/САМ | ✅ Проверено (VERIFY-001/002/003) | VERIFY-001 | ✅ Да |
| `scripts/blogger_page_parser.py` | МИГРАЦИЯ | ✅ Проверено (VERIFY-001/002/003) | VERIFY-001 | ✅ Да |
| `scripts/blogger_postid_rescue.py` | МИГРАЦИЯ | ✅ Проверено (VERIFY-001/002/003) | VERIFY-001 | ✅ Да |
| `scripts/image_storage_adapter.py` | САМ | ✅ Проверено (VERIFY-001/002/003) | VERIFY-001 | ✅ Да |
| `scripts/pdn_scanner.py` | САН | ✅ Проверено (VERIFY-001/002/003) | VERIFY-001 | ✅ Да |
| `scripts/sanitize_images.py` | САМ/СУМКа | ✅ Проверено (VERIFY-001/002/003) | VERIFY-001 | ✅ Да |
| `scripts/registry/sync_manifests.py` | САМ | ✅ Проверено (VERIFY-001/002/003); опубликовано в sanitized (REG-015, PR #2) | VERIFY-001 / REG-015 | ✅ Да |
| `scripts/sync_readme_licenses.py` | ЛИЦ | ✅ Проверено (VERIFY-001/002/003) | VERIFY-001 | ✅ Да |
| `scripts/sync_readme_sections.py` | САМ | ✅ Проверено (VERIFY-001/002/003) | VERIFY-001 | ✅ Да |
| `scripts/update_status.py` | САМ/СУМКа | ✅ Проверено (VERIFY-001/002/003) | VERIFY-001 | ✅ Да |
| `scripts/branch-protection.json` | САМ | ✅ Проверено (VERIFY-001/002/003) | VERIFY-003 | ✅ Да |
| `scripts/ruleset.json` | САМ | ✅ Проверено (VERIFY-001/002/003) | VERIFY-003 | ✅ Да |
| `scripts/ruleset-repo.json` | САМ | ✅ Проверено (VERIFY-001/002/003) | VERIFY-003 | ✅ Да |
| `.github/workflows/apply-architecture-patches.yml` | AGENTS | ✅ Проверено (VERIFY-001/002/003) | VERIFY-002 | ✅ Да |
| `.github/workflows/architecture-check.yml` | САМ | ✅ Проверено (VERIFY-001/002/003) | VERIFY-002 | ✅ Да |
| `.github/workflows/auto-update-status.yml` | САМ | ✅ Проверено (VERIFY-001/002/003) | VERIFY-002 | ✅ Да |
| `.github/workflows/license-check.yml` | ЛИЦ | ✅ Проверено (VERIFY-001/002/003) | VERIFY-002 | ✅ Да |
| `.github/workflows/manifest-consistency-check.yml` | INFRA | ✅ Проверено (VERIFY-001/002/003) | VERIFY-002 | ✅ Да |
| `.github/workflows/manifest-lint.yml` | INFRA | ✅ Проверено (VERIFY-001/002/003) | VERIFY-002 | ✅ Да |
| `.github/workflows/markdown-lint.yml` | INFRA | ✅ Проверено (VERIFY-001/002/003) | VERIFY-002 | ✅ Да |
| `.github/workflows/pr-prefix-check.yml` | AGENTS | ✅ Проверено (VERIFY-001/002/003) | VERIFY-002 | ✅ Да |
| `.github/workflows/readme-license-check.yml` | ЛИЦ | ✅ Проверено (VERIFY-001/002/003) | VERIFY-002 | ✅ Да |
| `.github/workflows/sync-manifests.yml` | САМ | ✅ Проверено (VERIFY-001/002/003) | VERIFY-002 | ✅ Да |
| `.github/workflows/sync-readme-sections.yml` | САМ | ✅ Проверено (VERIFY-001/002/003) | VERIFY-002 | ✅ Да |
| `.github/workflows/update-manifest-dates.yml` | САМ | ✅ Проверено (VERIFY-001/002/003) | VERIFY-002 | ✅ Да |
| `.github/workflows/update-status.yml` | САМ | ✅ Проверено (VERIFY-001/002/003) | VERIFY-002 | ✅ Да |
| `.github/PULL_REQUEST_TEMPLATE.md` | AGENTS | ✅ Проверено (VERIFY-001/002/003) | VERIFY-003 | ✅ Да |
| `docs/manifests.yaml` | САМ/README | ✅ Проверено (VERIFY-001/002/003) в legacy; superseded in sanitized by manifests/registry/manifests.yaml (REG-015), отсутствует в public/main | VERIFY-003 / REG-015 | ✅ Да |
| `docs/STATUS.md` | САМ/МИГРАЦИЯ/СУМКа | ✅ Проверено (VERIFY-001/002/003) | VERIFY-003 | ✅ Да |
| `.cursorrules` | САМ | ✅ Проверено (VERIFY-001/002/003) | VERIFY-003 | ✅ Да |
| `.markdownlint-cli2.jsonc` | INFRA | ✅ Проверено (VERIFY-001/002/003) | VERIFY-003 | ✅ Да |
| `.markdownlint.yaml` | INFRA | ✅ Проверено (VERIFY-001/002/003) | VERIFY-003 | ✅ Да |
| `.markdownlintignore` | INFRA | ✅ Проверено (VERIFY-001/002/003) | VERIFY-003 | ✅ Да |

### Блок Б: Отсутствует — имя определено (требуют создания)

Файлы, которых нет ни в одном репозитории (репозитории `shared-assets` и доменные удалены при сбросе 11.09.2026). Имя и путь известны из манифестов.

| Путь | Манифест | Статус | Задача | Имя определено |
| :--- | :--- | :---: | :--- | :---: |
| `generate_sitemaps.py` | СУМКа/ГРЕК-ПАНТЕОН | ❌ Отсутствует | MIG-013 | ✅ Да |
| `ping_search_engines.py` | СУМКа | ❌ Отсутствует | MIG-013 | ✅ Да |
| `image_sanitizer.py` | САМ | ❌ Отсутствует | MIG-013 | ✅ Да |
| `generate_redirect_map.py` | МИГРАЦИЯ | ❌ Отсутствует | MIG-020 | ✅ Да |
| `build_static_rss.py` | МИГРАЦИЯ | ❌ Отсутствует | MIG-020 | ✅ Да |
| `extract_original_author.py` | МИГРАЦИЯ | ❌ Отсутствует | MIG-020 | ✅ Да |
| `slug_optimizer.py` | МИГРАЦИЯ | ❌ Отсутствует | MIG-020 | ✅ Да |
| `video_link_processor.py` | МИГРАЦИЯ/САН | ❌ Отсутствует | *новая задача* | ✅ Да |
| `grekpanteon_pipeline.py` | ГРЕК-ПАНТЕОН | ❌ Отсутствует | MIG-021 | ✅ Да |
| `build_static_dump.py` | ГРЕК-ПАНТЕОН | ❌ Отсутствует | MIG-021 | ✅ Да |
| `build_astro_data.py` | ГРЕК-ПАНТЕОН | ❌ Отсутствует | MIG-021 | ✅ Да |
| `image_source_extractor.py` | ГРЕК-ПАНТЕОН | ❌ Отсутствует | MIG-021 | ✅ Да |
| `generate_causal_links.py` | ГРЕК-ПАНТЕОН | ❌ Отсутствует | MIG-021 | ✅ Да |
| `build_geojson_by_generation.py` | ГРЕК-ПАНТЕОН | ❌ Отсутствует | MIG-021 | ✅ Да |
| `monitor_daily_publication.py` | ГРЕК-ПАНТЕОН | ❌ Отсутствует | MIG-021 | ✅ Да |
| `rollback_publication.py` | ГРЕК-ПАНТЕОН | ❌ Отсутствует | MIG-021 | ✅ Да |
| `migrate_blogger_to_r2.py` | САМ/СУМКа | ❌ Отсутствует | MIG-010 | ✅ Да |
| `social_distribution_worker.js` | СУМКа | ❌ Отсутствует | *новая задача* | ✅ Да |
| `shared-assets/identity_graph.json` | САМ, СУМКа | ❌ Отсутствует | INFRA-010 | ✅ Да |
| `shared-assets/video_alternatives_db.json` | САМ, СУМКа | ❌ Отсутствует | INFRA-010 | ✅ Да |
| `shared-assets/blogger_image_metadata.json` | САМ, СУМКа | ❌ Отсутствует | INFRA-010 | ✅ Да |
| `shared-assets/config/verification.json` | САМ, СУМКа | ❌ Отсутствует | INFRA-010 | ✅ Да |
| `shared-assets/config/social_links.json` | САМ, СУМКа | ❌ Отсутствует | INFRA-010 | ✅ Да |
| `shared-assets/config/image_storage_routing.json` | САМ, СУМКа | ❌ Отсутствует | INFRA-010 | ✅ Да |
| `shared-assets/config/social_communities_seed.json` | СУМКа | ❌ Отсутствует | INFRA-010 | ✅ Да |
| `shared-assets/components/PrivacyPolicyLink.js` | САМ | ❌ Отсутствует | INFRA-010 | ✅ Да |
| `shared-assets/components/MultiVolumeNavigation.js` | МИГРАЦИЯ | ❌ Отсутствует | INFRA-010 | ✅ Да |
| `shared-assets/components/StickyBottomBar.js` | МИГРАЦИЯ | ❌ Отсутствует | INFRA-010 | ✅ Да |
| `shared-assets/adapters/SocialDistributionAdapter.js` | СУМКа | ❌ Отсутствует | INFRA-010 | ✅ Да |
| `shared-assets/widgets/feedback-simple.js` | МИГРАЦИЯ | ❌ Отсутствует | INFRA-010 | ✅ Да |
| `shared-assets/schemas/book-chapter.jsonld` | МИГРАЦИЯ | ❌ Отсутствует | INFRA-010 | ✅ Да |
| `shared-assets/templates/layout.html` | МИГРАЦИЯ | ❌ Отсутствует | INFRA-010 | ✅ Да |
| `{каждый_сайт}/migration_seo_map.json` | МИГРАЦИЯ, САН, ГРЕК-ПАНТЕОН | ❌ Отсутствует | MIG-020, MIG-021 | ✅ Да |
| `{каждый_сайт}/media_passport.json.gz` | САМ, МИГРАЦИЯ, ГРЕК-ПАНТЕОН | ❌ Отсутствует | MIG-013 | ✅ Да |
| `{каждый_сайт}/authors_override.json` | МИГРАЦИЯ | ❌ Отсутствует | MIG-020 | ✅ Да |
| `{каждый_сайт}/ai-hints.txt` | СУМКа, ГРЕК-ПАНТЕОН | ❌ Отсутствует | MIG-020, MIG-021 | ✅ Да |
| `docs/DEVELOPMENT_TOOLS.md` | САМ/СУМКа | ❌ Отсутствует | INFRA-004 | ✅ Да |
| `docs/IMAGE_SANITIZATION_GUIDE.md` | САМ | ❌ Отсутствует | INFRA-004 | ✅ Да |
| `docs/BLOGGER_IMAGE_STORAGE_GUIDE.md` | САМ/СУМКа | ❌ Отсутствует | INFRA-004 | ✅ Да |
| `docs/SOCIAL_DISTRIBUTION_GUIDE.md` | СУМКа | ❌ Отсутствует | INFRA-004 | ✅ Да |
| `docs/SOCIAL_COMMUNITY_MANAGEMENT.md` | СУМКа | ❌ Отсутствует | INFRA-004 | ✅ Да |
| `docs/SEARCH_CONSOLE_SETUP.md` | СУМКа | ❌ Отсутствует | INFRA-004 | ✅ Да |
| `docs/SITEMAP_GENERATION_GUIDE.md` | СУМКа | ❌ Отсутствует | INFRA-004 | ✅ Да |
| `docs/SLUG_OPTIMIZATION_QUEUE.json` | МИГРАЦИЯ | ❌ Отсутствует | INFRA-004 | ✅ Да |
| `.github/workflows/backup_blogger_metadata.yml` | САМ/СУМКа | ❌ Отсутствует | INFRA-012 | ✅ Да |
| `.github/workflows/backup-content.yml` | САМ | ❌ Отсутствует | INFRA-012 | ✅ Да |
| `.github/workflows/publish-assets.yml` | САМ | ❌ Отсутствует | INFRA-012 | ✅ Да |
| `.github/workflows/ai-rules-sync.yml` | САМ | ❌ Отсутствует | INFRA-012 | ✅ Да |
| `.github/workflows/protocol-check.yml` | AGENTS | ❌ Отсутствует | INFRA-012 | ✅ Да |
| `.github/copilot-instructions.md` | САМ §3.3.5 | ❌ Отсутствует | INFRA-012 | ✅ Да |
| `legal/privacy-policy.html` | САМ | ❌ Отсутствует | INFRA-103 | ✅ Да |
| `hugo/layouts/shortcodes/img.html` | МИГРАЦИЯ/СУМКа | ❌ Отсутствует | INFRA-104 | ✅ Да |
| `scripts/validate_redirect_map.py` | МИГРАЦИЯ | ❌ Отсутствует | INFRA-106 | ✅ Да |

### Блок В: Отсутствует — концепты (имя не определено)

Требования к функциональности, для которых **ещё не определено** имя файла, путь и интерфейс**. Перед созданием требуется отдельная задача проектирования.

| Назначение | Манифест | Принцип/Раздел | Статус | Задача | Имя определено |
| :--- | :--- | :--- | :---: | :--- | :---: |
| Скрипт троттлинга публикаций (200/сутки) | САМ | Принцип 2.6 | ❌ Отсутствует | *новая задача* | ❌ Нет |
| ИИ-агент Технический писатель | САМ | Принцип 2.11 | ❌ Отсутствует | *новая задача* | ❌ Нет |
| Скрипт зомби-аудита (Data Decay) | САМ | Принцип 3.6 | ❌ Отсутствует | *новая задача* | ❌ Нет |
| Таблицы БД: журнал транзакций, журнал доступа к ПДн, журнал соц-постов, неудачные строки извлечения | САМ | Принцип 3.14 | ❌ Отсутствует | *новая задача* | ❌ Нет |
| Скрипт аварийной миграции с Блоггера в Р2 | САМ | Принцип 3.21 | ❌ Отсутствует | MIG-010 | ❌ Нет |
| ИИ-агент инспектор контента (детекция фрода) | СУМКа | Раздел 11.3 | ❌ Отсутствует | *новая задача* | ❌ Нет |
| Скрипт генерации тематического паспорта | СУМКа | Раздел 3 | ❌ Отсутствует | MIG-013 | ❌ Нет |
| Конвейер санитарной обработки изображений (как компонент) | СУМКа | Раздел 5.6 | ❌ Отсутствует | MIG-013 | ❌ Нет |
| Адаптер MinIO ETL | САН | Раздел 1.3 | ❌ Отсутствует | INFRA-010 | ❌ Нет |
| Системный промпт для ИИ-конвейера Пантеона | ГРЕК-ПАНТЕОН | Раздел 4.1 | ❌ Отсутствует | MIG-021 | ❌ Нет |
| Hugo-шаблон image-with-source.html | ГРЕК-ПАНТЕОН | Раздел 7.3 | ❌ Отсутствует | MIG-021 | ❌ Нет |
| Mobile-First макет layout.html | МИГРАЦИЯ | Раздел 5.1.1.7 | ❌ Отсутствует | MIG-020 | ❌ Нет |
| Скрипт генерации статических страниц Пантеона | МИГРАЦИЯ | Раздел 5.1.3 | ❌ Отсутствует | MIG-021 | ❌ Нет |
| Скрипт миграции между слоями хранения | САМ | Принцип 4.9 | ❌ Отсутствует | MIG-010 | ❌ Нет |

---

## 📚 Источники требований и юридические документы (не артефакты)

Эти файлы **не являются артефактами** (это нормативные документы и источники требований). Их состояние отслеживается через workflows `update-manifest-dates.yml` и `sync-readme-sections.yml`.

| Файл | Назначение |
| :--- | :--- |
| `САМ.md` | Системный Архитектурный Манифест (высший приоритет) |
| `САН.md` | Манифест платформы САН |
| `СУМКа.md` | Манифест системы управления медиа-контентом |
| `ГРЕК-ПАНТЕОН.md` | Манифест базы знаний по античной мифологии |
| `МИГРАЦИЯ.md` | План миграции 15 доменов |
| `ЛИЦ.md` | Лицензионный пакет |
| `AGENTS.md` | Инструкции для ИИ-агентов |
| `ВАКУУМНЫЙ_КОНДЕНСАТ.md` | Манифест научного портала (Greenfield) |
| `README.md` | Описание репозитория и сводная таблица манифестов |
| `STATUS.md` (корень) | Операционное состояние экосистемы (автогенерируется) |
| `LICENSE` | Лицензия для кода (AGPLv3) |
| `LICENSE-CONTENT` | Лицензия для контента (CC BY-NC 4.0) |

---

## Процесс обновления реестра

1. Закрыт протокол (смержен PR) → ИИ-агент обновляет `TASKS.md` (статусы, Реестр артефактов).
2. Человек-подтверждение (Основатель) проверяет и фиксирует.
3. Автосинхронизация в `STATUS.md`, `manifests/registry/manifests.yaml`, `README.md`.

## Дизайн-система и финализация пилота (INFRA-074–100)

- [x] INFRA-074: tap-target 44px скоуп (навигация/кнопки); инлайн-ссылки в потоке текста (тело статей, описания и заголовки карточек) -> display:inline; min-height:0
- [x] INFRA-075–076: дизайн-токены + фикс загрузки (link в head вместо @import)
- [x] INFRA-077: карточки постов, горизонтальная шапка, cookie-баннер
- [x] INFRA-078–079: контейнеры, полноширинные полосы, колонка чтения 75ch
- [x] INFRA-080: бренд-шапка (h1+теглайн без дубля), теги-ссылки, индиго-полосы
- [x] INFRA-081: модульная шкала типографики (норматив в СУМКа)
- [x] INFRA-084: бар индиго, cookie над баром, шрифт PT Sans/Serif
- [x] INFRA-085: чёрный cookie-баннер, safe-area
- [x] INFRA-086: drawer над cookie, горизонтальное меню
- [x] INFRA-087: промежуточный пресет Вариант А
- [x] INFRA-088: итоговая типографика (веса 400/700, тело 18px, h1 28px)
- [x] INFRA-089: медиа-радиус как блоки, бренд 22px
- [x] INFRA-090: логотип в шапке (params.logo + SVG-fallback), фикс .brand row, санитария FETCH_HEAD
- [x] INFRA-092: двухцветие названия + янтарная линия
- [x] INFRA-093: адаптивный бар (portrait снизу / landscape справа) — отменён по решению Основателя
- [x] INFRA-094: фикс линии по тексту (094a), revert 093, пропорции логотипа (094b), увеличение логотипа (094c/d)
- [x] INFRA-095: меню column везде + flex-wrap
- [x] INFRA-097: Pagefind в подкаталоге Pages: glob **/index.html; изоляция контента data-pagefind-body условно по .Kind==page (листинги/главная/таксономии вне индекса); клиентский фразовый режим против шума предлогов; data-pagefind-weight на h1
- [x] INFRA-098: убрана стандартная подсветка ссылок при тапе на мобильных
- [x] INFRA-100: тёмная тема — persistence выбора, логотип WebP 5.5 КБ, контраст подзаголовка и элементов поиска (PageSpeed Accessibility 100/100)

- [x] Оригиналы изображений пилота (перескачка из Blogger, 2026-09-22)
- [ ] INFRA-082: Sticky Bottom Bar (моб.) + полировка (focus-states, CLS)
- [ ] INFRA-083: rollout-план 12 сайтов (порядок, чек-листы, откат)

## 📅 Приоритизация этапов (Обновлено: 2026-11-09)

### 🔥 Фаза 1: Миграция Контента (CURRENT PRIORITY)

Цель: Перенести текст и структуру 13 сайтов с Blogger на Hugo.
Стратегия медиа: **Link Preservation** (сохранение ссылок на googleusercontent).

| ID | Название | Описание | Приоритет | Статус |
| :--- | :--- | :--- | :--- | :--- |
| **MIG-CORE-EXECUTE** | Массовый парсинг Blogger API | Извлечение постов, конвертация в Markdown, сохранение img src как есть. | 🔴 CRITICAL | ⬜ TODO |
| **MIG-HUGO-THEME** | Адаптация темы Hugo | Настройка шаблонов для отображения legacy-контента. | 🟠 HIGH | ⬜ IN PROGRESS |

### ⏸️ Фаза 2: Инфраструктура Хранения (DEFERRED)

Цель: Изоляция данных от зависимостей Google. Активируется ТОЛЬКО после успеха Фазы 1.
Стратегия медиа: **Asset Consolidation** (перенос в Cloudflare R2).

| ID | Название | Причина отложенности | Статус |
| :--- | :--- | :--- | :--- |
| **INFRA-R2-SETUP** | Создание бакета Cloudflare R2 | Не требуется для текущей миграции текста. Блокирует ресурсы. | ⏸️ DEFERRED |
| **DEV-R2-LIBRARY** | Скрипт r2_uploader.py | Инструмент готов, но внедрение преждевременно. | ⏸️ DEFERRED |
| **MIG-SAN-R2** | Перенос картинок САН в R2 | Требует завершенной миграции сайта САН на Hugo. | ⏸️ BLOCKED BY PHASE 1 |
| **MIG-PANTEON-R2** | Перенос картинок Пантеона в R2 | Требует завершенной миграции сайта Пантеон на Hugo. | ⏸️ BLOCKED BY PHASE 1 |

## Задачи по результатам аудита пилотных репозиториев (2026-10-11)

### INFRA-119: Добавить favicon.ico в obrazslov

- **Репозиторий:** blago-nko/obrazslov
- **Приоритет:** Высокий
- **Статус:** ⬜ Не начато
- **Описание:** Создать static/favicon.ico для соответствия требованиям пилота
- **Критерии приёмки:** Файл существует и отображается в браузере
- **Связанные задачи:** MIG-002

### INFRA-120: Добавить manifest.json в obrazslov

- **Репозиторий:** blago-nko/obrazslov
- **Приоритет:** Средний
- **Статус:** ⬜ Не начато
- **Описание:** Создать static/manifest.json для PWA поддержки
- **Критерии приёмки:** Валидный JSON с необходимыми полями (name, short_name, start_url, display, icons)
- **Связанные задачи:** MIG-002

### INFRA-121: Обновить .gitignore в obrazslov

- **Репозиторий:** blago-nko/obrazslov
- **Приоритет:** Низкий
- **Статус:** ⬜ Не начато
- **Описание:** Добавить исключение pagefind/ в .gitignore
- **Критерии приёмки:** pagefind/ присутствует в .gitignore
- **Связанные задачи:** MIG-002

### INFRA-122: Обновить .gitignore в manifests

- **Репозиторий:** blago-nko/manifests
- **Приоритет:** Низкий
- **Статус:** ⬜ Не начато
- **Описание:** Добавить исключения public/ и pagefind/ в .gitignore
- **Критерии приёмки:** public/ и pagefind/ присутствуют в .gitignore
- **Связанные задачи:** INFRA-034

### INFRA-123: Обновить .gitignore в shared-assets

- **Репозиторий:** blago-nko/shared-assets
- **Приоритет:** Низкий
- **Статус:** ⬜ Не начато
- **Описание:** Добавить исключения public/ и pagefind/ в .gitignore
- **Критерии приёмки:** public/ и pagefind/ присутствуют в .gitignore
- **Связанные задачи:** INFRA-050

---

## Реестры manifests/registry (operational-контур REG-)

> **Временный operational-префикс `REG-`** для машиночитаемых реестров `manifests/registry/`.
> Нормативное утверждение префикса в `САМ.md` §1.5 и в `pr-prefix-check.yml` — задача **REG-009** (требует 👤 подтверждения Основателя).
> До утверждения `REG-` используется только в этом разделе и в git-истории Батч 2; остальные протоколы продолжают использовать каноничные префиксы САМ §1.5.
> Батч 2 выполнен в legacy локальной истории; в публичном sanitized tree история начинается с initial commit.
> Нормативные `.md`-манифесты в этом батче НЕ изменяются.

### Выполнено

| ID | Задача | Артефакт | Приор. | Ответств. | Статус | Комментарий |
| :--- | :--- | :--- | :---: | :--- | :---: | :--- |
| **REG-001** | `ownership.yaml` | `manifests/registry/ownership.yaml` | 🔴 | 🤖→👤 | ✅ | источник в restricted backup; право собственности / withdrawal procedure |
| **REG-002** | `identity_graph.public.yaml` | `manifests/registry/identity_graph.public.yaml` | 🔴 | 🤖→👤 | ✅ | источник в restricted backup; sanitized tree без legacy history; public_minimized на базе письменного заявления |
| **REG-003** | `documentation.yaml` | `manifests/registry/documentation.yaml` | 🟠 | 🤖→👤 | ✅ | источник в restricted backup; JSON-LD consent-aware, status_drift, video privacy_insight |
| **REG-004** | `artifacts.yaml` | `manifests/registry/artifacts.yaml` | 🟠 | 🤖→👤 | ✅ | источник в restricted backup; mapping 21+13+6+5=45, secrets never_in_git |
| **REG-005** | `feature_flags.yaml` | `manifests/registry/feature_flags.yaml` | 🟠 | 🤖→👤 | ✅ | коммит `restricted backup`; stage-gated флаги, embed/privacy gates, deploy gates |
| **REG-006** | `comment_policy.yaml` | `manifests/registry/comment_policy.yaml` | 🟠 | 🤖→👤 | ✅ | коммит `restricted backup`; архив комментариев, no auto PII-scan, giscus-with-consent |
| **REG-007** | `product_catalog.yaml` | `manifests/registry/product_catalog.yaml` | 🟠 | 🤖→👤 | ✅ | коммит `restricted backup`; некоммерческая терминология, ND-политика, Offer stage 1+ |
| **REG-008** | `derived_summaries.state_service_years` (точная формула 6+4=10) | `manifests/registry/identity_graph.public.yaml` | 🔴 | 🤖→👤 | ✅ | источник в restricted backup; municipal_administration 6 + military_service_credit x2 = 4 |
| **REG-014** | Починить `update_status.py`: пути + draft ⚪ + динамические цели + docstring к факту | `scripts/registry/update_status.py` | 🔴 | 🤖→👤 | ✅ | выполнено: пути `manifests/registry/*`, динамические счётчики без хардкода 14/7, `⚪` для draft, docstring синхронизирован с `DD.MM.YYYY (UTC)`; опубликовано в `325d005` и `5ec0448` |

### Активные

| ID | Задача | Артефакт / цель | Приор. | Ответств. | Статус | Комментарий |
| :--- | :--- | :--- | :---: | :--- | :---: | :--- |
| **REG-009** | Утвердить префикс `REG-` в `САМ.md` §1.5 и в `pr-prefix-check.yml` | `manifests/САМ.md`, `.github/workflows/pr-prefix-check.yml` | 🔴 | 👤 | ⬜ | Нормативное решение Основателя; до этого `REG-` — временный operational-префикс; `САМ.md` НЕ правим |
| **REG-010** | Создать корневой `README.md` монорепы | `README.md` | 🔴 | 🤖→👤 | ⬜ | Сейчас пустой tracked-файл; структура + лицензии + принципы |
| **REG-011** | Восстановить `.gitignore` под монорепу | `.gitignore` | 🟠 | 🤖 | ⬜ | Сейчас пустой tracked-файл; Python/Hugo/Astro/Node/секрети; не влияет на уже отслеженные archive |
| **REG-012** | Восстановить `.markdownlint-cli2.jsonc` | `.markdownlint-cli2.jsonc` | 🟡 | 🤖 | ⬜ | Сейчас пустой tracked-файл; MD013/MD033/MD041 relax, ignores сгенерированных каталогов |
| **REG-013** | Interim-перегенерация `docs/STATUS.md` из реестров | `docs/STATUS.md` | 🔴 | 🤖→👤 | ✅ | закреплено как постоянный контракт после REG-014/REG-015: `update_status.py` — единственный писатель `docs/STATUS.md` (INFRA-029), `sync_manifests.py` не пишет STATUS; interim-значения `Реестров YAML = 16`, `Машиночитаемых реестров = 16`, VAC `⚪`, источники `manifests/registry/*` подтверждены |
| **REG-015** | Починить `sync_manifests.py`: REGISTRY path + related links + draft icon | `scripts/registry/sync_manifests.py` | 🟠 | 🤖→👤 | ✅ | выполнено: source of truth `manifests/registry/manifests.yaml`; PR #1 (база/STATUS-risk, `7675bc4`/`58567ba`), PR #2 (related/draft, `e468b61`, SHA `0de26bea1ae1cb35bb8d9a8ac2ef53196dcae08850de3e96d60ffbddec434bca`), PR #3 (README align, `b688fa7`); INFRA-029 сохранён: sync не пишет `docs/STATUS.md`; `related_block` uses `relative_to(current_dir)`, honors `related_title`, draft `⚪` |
| **REG-016** | Перенос 21 script/config `archive` -> `scripts/` | `scripts/` | 🟠 | 🤖→👤 | ⬜ | Только после ревью; см. `artifacts.yaml` script_mapping |
| **REG-017** | Перенос 13 workflows `archive` -> `.github/workflows/` | `.github/workflows/` | 🟠 | 🤖→👤 | ⬜ | Обновить префиксы после REG-009; включить tests.yml, update-status.yml, pr-prefix-check.yml |
| **REG-018** | Перенос 6 тестов `archive` -> `tests/` + обновление snapshot | `tests/` | 🟠 | 🤖→👤 | ⬜ | Пути `scripts/registry/update_status.py`; секция `Состояние N доменов` динамически (сейчас ждёт 14, станет 15) |
| **REG-019** | Решить судьбу пустых `LICENSE-CODE` / `LICENSE-TEXT` | корень | 🟡 | 👤 | ⬜ | Указать на `LICENSE` / `LICENSE-CONTENT` или удалить; не дублировать тексты лицензий |
| **REG-020** | Применить `domain_rename_map.yaml` через `rename_domains.py` | `manifests/registry/domain_rename_map.yaml` | 🟡 | 🤖→👤 | ⬜ | НЕ вручную (`do_not_apply_manually: true`); после создания скрипта и проверки DNS/301 |

### Зависимости и порядок

    REG-009 (утверждение префикса) --> REG-017 (перенос workflows с pr-prefix-check)
    REG-014/015 (починка генераторов) --> REG-013 закрепляется как постоянный контракт
    REG-016/017/018 (перенос archive) --> Python-контур становится исполняемым в CI
    REG-020 (rename) --> только после REG-016 (rename_domains.py в scripts/)

> Примечание: `INFRA-119...123` в этом файле заняты задачами пилотов (favicon/manifest/.gitignore). Реестровый контур сознательно отделён префиксом `REG-`, чтобы не смешивать инфраструктуру сайтов и машиночитаемые реестры экосистемы. Нормативные `.md`-манифесты в Батч 3.1 не изменяются.
