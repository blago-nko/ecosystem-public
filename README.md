# blago-nko / ecosystem

Моно-репозиторий нормативных манифестов, машиночитаемых реестров и операционного контура экосистемы Некоммерческого партнёрства «Общественное благополучие Воронежа».

Экосистема реализует общественно значимые проекты в сферах историко-биографического просвещения, образования, поддержки гражданских инициатив, развития агентского сообщества в недвижимости и фундаментальной науки.

## Структура

| Путь | Назначение |
| :--- | :--- |
| manifests/ | Нормативные .md-манифесты: САМ, САН, СУМКа, ГРЕК-ПАНТЕОН, МИГРАЦИЯ, ЛИЦ, AGENTS, ВАКУУМНЫЙ_КОНДЕНСАТ |
| manifests/registry/ | Машиночитаемые operational-реестры, 16 YAML-файлов |
| docs/ | Автогенерируемый статус экосистемы, docs/STATUS.md |
| archive/legacy-scripts/ | Архив скриптов и конфигов, переносится в scripts/, REG-016 |
| archive/legacy-github/ | Архив workflows и шаблонов, переносится в .github/, REG-017 |
| archive/legacy-tests/ | Архив тестов и фикстур, переносится в tests/, REG-018 |
| archive/legacy-docs/ | Архив документации старого репозитория |
| audits/ | Аудиты и заметки о переносе и drift |
| scripts/, tests/, .github/workflows/ | Опубликован operational skeleton: update_status.py (REG-014), sync_manifests.py (REG-015), STATUS tests, update-status workflow и GitHub config placeholders; apply_l0_contour.py и validation harness остаются в restricted/ORIG контуре до REG-016..018 |
| sites/, apps/, shared-assets/ | Целевые каталоги сайтов, приложений и общих ассетов |

## Реестры manifests/registry/

Машиночитаемый слой экосистемы. Используется временный operational-префикс REG-. Нормативное утверждение префикса — задача REG-009.

    artifacts.yaml          mapping легаси-артефактов в целевые пути, secrets policy
    comment_policy.yaml     политика комментариев: архив Blogger, giscus-with-consent
    crypto_policy.yaml      криптоконтур, RF PII gateway, запреты plaintext
    documentation.yaml      правила документации, JSON-LD consent-aware, status_drift
    domain_rename_map.yaml  интент переименования доменов, pending, не применять вручную
    domains-graph.yaml      граф доменов и связей, Протокол 016 САМ
    feature_flags.yaml      stage-gated флаги, embed/privacy/deploy gates
    identity_graph.public.yaml     персона, роль, источник правды, public_minimized
    legal_routes.yaml       юридические маршруты
    manifests.yaml          реестр нормативных .md-манифестов, 8 записей
    ownership.yaml          право собственности и withdrawal procedure
    product_catalog.yaml    некоммерческие уровни участия и каталог сервисов
    rights_registry.yaml    лицензии и права на исходные материалы
    stage_map.yaml          карта этапов экосистемы
    storage_policy.yaml     политика хранения: Blogger, R2, Git
    terminology.yaml        каноничная терминология

## Нормативные манифесты

| Манифест | Файл | Префикс, САМ параграф 1.5 |
| :--- | :--- | :--- |
| Системный Архитектурный Манифест | manifests/САМ.md | SAM- |
| Манифест САН | manifests/САН.md | CAN- |
| Манифест СУМКа | manifests/СУМКа.md | SUMKA- |
| Манифест ГРЕК-ПАНТЕОН | manifests/ГРЕК-ПАНТЕОН.md | GP- |
| Манифест МИГРАЦИЯ | manifests/МИГРАЦИЯ.md | MIG- |
| Лицензионный Пакет | manifests/ЛИЦ.md | LIC- |
| Инструкции для ИИ-агентов | manifests/AGENTS.md | — |
| Манифест ВАКУУМНЫЙ_КОНДЕНСАТ | manifests/ВАКУУМНЫЙ_КОНДЕНСАТ.md | VAC- |

## Лицензии

| Слой | Файл | Лицензия |
| :--- | :--- | :--- |
| Код | LICENSE | GNU AGPLv3 |
| Контент | LICENSE-CONTENT | CC BY-NC 4.0 |
| Исключение для науки VAC | текст / код | CC BY 4.0 / MIT |

Подробности находятся в manifests/ЛИЦ.md и manifests/registry/rights_registry.yaml. Пустые LICENSE-CODE и LICENSE-TEXT оставлены как есть до решения Основателя по задаче REG-019. Дублировать тексты лицензий не нужно.

## Принципы экосистемы

- надёжность перед скоростью;
- приватность перед автоматизацией: ПДн только через RF gateway, plaintext запрещён;
- stage-gated features: manifests/registry/stage_map.yaml и manifests/registry/feature_flags.yaml;
- некоммерческая терминология: уровни участия, взнос, партнёрское соглашение, аналитические материалы;
- без публичных формулировок тариф, цена, продажа, прайс-лист для НКО-сервисов;
- сохранение ссылок при миграции: Link Preservation до Asset Consolidation;
- единый источник правды и кросс-манифестная синхронизация: Протокол 016, САМ параграф 3.1.

## Текущее состояние

Монорепа формируется. Опубликован минимальный operational skeleton: scripts/registry/update_status.py, scripts/registry/sync_manifests.py, tests/, .github/workflows/update-status.yml и GitHub config placeholders. sync_manifests.py опубликован в sanitized-контуре (REG-015); apply_l0_contour.py и validation harness остаются в restricted/ORIG контуре и не публикуются как есть до REG-016..018. Legacy-архивы archive/legacy-* сохраняются до завершения переноса по задачам REG-016..018. docs/STATUS.md генерируется scripts/registry/update_status.py и согласован с машиночитаемыми реестрами.

Живые метрики: docs/STATUS.md. Реестр задач: TASKS.md. Долгосрочный план: ROADMAP.md. Инструкции агентам: manifests/AGENTS.md.

## Вклад

См. CONTRIBUTING.md, CODE_OF_CONDUCT.md, SECURITY.md. Изменения манифестов вносятся только через протокол архитектурных изменений с каноничными префиксами, САМ параграф 1.5 и параграф 2.1.
