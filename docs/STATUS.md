# 📈 Статус документов

> ⚠️ **Этот файл обновляется автоматически** через GitHub Actions
> (`.github/workflows/update-status.yml`). Не редактируйте вручную.
> Реестр задач: [TASKS.md](../TASKS.md). Долгосрочный план: [ROADMAP.md](../ROADMAP.md).

---

## Текущее состояние

| # | Манифест | Файл | Версия | Дата | Статус | Протоколов |
|:-:|:---------|:-----|:------:|:----:|:------:|:----------:|
| 1 | САМ | `manifests/САМ.md` | 2.15-н | 2026-11-09 | 🟢 | 3 |
| 2 | СУМКа | `manifests/СУМКа.md` | 1.11-н | 2026-09-24 | 🟢 | 1 |
| 3 | САН | `manifests/САН.md` | 1.6-н | 2026-09-24 | 🟢 | 1 |
| 4 | ГРЕК-ПАНТЕОН | `manifests/ГРЕК-ПАНТЕОН.md` | 1.10-н | 2026-09-16 | 🟢 | 1 |
| 5 | МИГРАЦИЯ | `manifests/МИГРАЦИЯ.md` | 1.16-н | 2026-11-09 | 🟢 | 2 |
| 6 | ЛИЦ | `manifests/ЛИЦ.md` | 1.9-н | 2026-11-09 | 🟢 | 2 |
| 7 | AGENTS | `manifests/AGENTS.md` | 1.10-н | 2026-11-09 | 🟢 | 2 |
| 8 | ВАКУУМНЫЙ_КОНДЕНСАТ | `manifests/ВАКУУМНЫЙ_КОНДЕНСАТ.md` | 0.1.0-draft | 2026-11-09 | ⚪ | 1 |

---

## Легенда статусов

| Иконка | Значение |
|:------:|:---------|
| 🟢 | Активен, актуален |
| 🟡 | Требует обновления |
| 🔴 | Устарел / конфликтует |
| ⚪ | Черновик |

---

## Состояние 15 доменов

> Источник: `manifests/registry/domains-graph.yaml` (Протокол 016 САМ). Инфраструктурных поддоменов: 1.

| # | Домен | Роль | Контур | Движок | Хостинг | Статус |
|:-:|:------|:-----|:------:|:------:|:-------:|:------:|
| 1 | blagorussia.ru | rss-hub | A | Hugo | GitHub Pages | 🟢 |
| 2 | obrazslov.ru | rss-site | A | Hugo | GitHub Pages | 🟢 |
| 3 | partnerstvo.blagorussia.ru | rss-site | A | Hugo | GitHub Pages | 🟢 |
| 4 | novosti.blagorussia.ru | rss-site | A | Hugo | GitHub Pages | 🟢 |
| 5 | ot-gorozan.blagorussia.ru | rss-site | A | Hugo | GitHub Pages | 🟢 |
| 6 | obavlenia.blagorussia.ru | rss-site | A | Hugo | GitHub Pages | 🟢 |
| 7 | interesnye-mesta.obrazslov.ru | rss-site | A | Hugo | GitHub Pages | 🟢 |
| 8 | moisites.blagorussia.ru | rss-site | A | Hugo | GitHub Pages | 🟢 |
| 9 | joga.blagorussia.ru | rss-site | A | Hugo | GitHub Pages | 🟢 |
| 10 | ideologia.obrazslov.ru | rss-site | A | Hugo | GitHub Pages | 🟢 |
| 11 | nasa-istoria.blagorussia.ru | rss-site | A | Hugo | GitHub Pages | 🟢 |
| 12 | grekpanteon.obrazslov.ru | knowledge-base | A | Astro | GitHub Pages | 🟢 |
| 13 | science.obrazslov.ru | research-portal | A | Astro | GitHub Pages | 🟢 |
| 14 | can.blagorussia.ru | pdn-platform | B | Next.js | Vercel | 🟢 |
| 15 | gallery.obrazslov.ru | nko-vitrina | V | Blogger | Blogger | 🟢 |

> Known drift: `science.obrazslov.ru` и `r2.blagorussia.ru` соответствуют pending-интенту `manifests/registry/domain_rename_map.yaml`. Применение — только через `rename_domains.py` (REG-020), не вручную (`do_not_apply_manually: true`).

---

## Состояние манифестов

> Источник: `manifests/registry/manifests.yaml`

| Манифест | Версия | Дата последней редакции | Статус | Протоколов |
|:---------|:------:|:-----------------------:|:------:|:----------:|
| САМ | 2.15-н | 2026-11-09 | 🟢 | 3 |
| СУМКа | 1.11-н | 2026-09-24 | 🟢 | 1 |
| САН | 1.6-н | 2026-09-24 | 🟢 | 1 |
| ГРЕК-ПАНТЕОН | 1.10-н | 2026-09-16 | 🟢 | 1 |
| МИГРАЦИЯ | 1.16-н | 2026-11-09 | 🟢 | 2 |
| ЛИЦ | 1.9-н | 2026-11-09 | 🟢 | 2 |
| AGENTS | 1.10-н | 2026-11-09 | 🟢 | 2 |
| ВАКУУМНЫЙ_КОНДЕНСАТ | 0.1.0-draft | 2026-11-09 | ⚪ | 1 |

---

## Машиночитаемые реестры

> Источник: `manifests/registry/*.yaml` (operational-контур REG-). Отдельный слой от нормативных .md-манифестов; не смешивать манифесты и реестры.

| Метрика | Значение |
| :-------- | :--------: |
| Реестров YAML | 16 |
| Нормативных .md-манифестов | 8 |
| Контентных доменов | 15 |
| Инфраструктурных поддоменов | 1 |

---

## Ключевые метрики

| Метрика | Значение | Цель |
|:--------|:--------:|:----:|
| Доменов в экосистеме (контентных) | 15 | 15 |
| Манифестов всего | 8 | 8 |
| Манифестов активно | 7 | 7 |
| Манифестов черновиков | 1 | 1 |
| Машиночитаемых реестров | 16 | 16 |
| Успешность автообновления STATUS.md | ≥99% | ≥99% |

---

## Активные риски

| # | Риск | Вероятность | Влияние | Митигация |
|:-:|:-----|:-----------:|:-------:|:----------|
| 1 | Таксономия domains-graph пуста (INFRA-020) | Высокая | Средняя | Задача в реестре |
| 2 | sync_manifests.py содержит блок записи STATUS (нарушает INFRA-029); требует полного ревью | Высокая | Высокая | REG-015 |
| 3 | domain_rename_map.yaml pending; science.obrazslov.ru / r2.blagorussia.ru как known drift | Средняя | Средняя | REG-020 |
| 4 | Пустые tracked LICENSE-CODE / LICENSE-TEXT | Низкая | Низкая | REG-019 |
| 5 | Runtime-валидация update_status.py отложена до CI (Python локально недоступен) | Высокая | Средняя | REG-017 после push |

**Последнее обновление**: 22.11.2026
