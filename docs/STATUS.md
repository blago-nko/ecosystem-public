# 📈 Статус документов

> ⚠️ Файл должен обновляться автоматически через `.github/workflows/update-status.yml` после переноса workflow (REG-017) и починки `scripts/registry/update_status.py` (REG-014).
> До этого он перегенерируется interim-методом из реестров `manifests/registry/`. Не редактируйте вручную без corresponding задачи.
> Реестр задач: [TASKS.md](../TASKS.md). Долгосрочный план: [ROADMAP.md](../ROADMAP.md).

---

## Текущее состояние

| # | Манифест | Файл | Версия | Дата | Статус | Протоколов |
| :-: | :--------- | :----- | :------: | :----: | :------: | :----------: |
| 1 | САМ | `САМ.md` | 2.15-н | 2026-11-09 | 🟢 | 3 |
| 2 | СУМКа | `СУМКа.md` | 1.11-н | 2026-09-24 | 🟢 | 1 |
| 3 | САН | `САН.md` | 1.6-н | 2026-09-24 | 🟢 | 1 |
| 4 | ГРЕК-ПАНТЕОН | `ГРЕК-ПАНТЕОН.md` | 1.10-н | 2026-09-16 | 🟢 | 1 |
| 5 | МИГРАЦИЯ | `МИГРАЦИЯ.md` | 1.16-н | 2026-11-09 | 🟢 | 2 |
| 6 | ЛИЦ | `ЛИЦ.md` | 1.9-н | 2026-11-09 | 🟢 | 2 |
| 7 | AGENTS | `AGENTS.md` | 1.10-н | 2026-11-09 | 🟢 | 2 |
| 8 | ВАКУУМНЫЙ_КОНДЕНСАТ | `ВАКУУМНЫЙ_КОНДЕНСАТ.md` | 0.1.0-draft | 2026-11-09 | ⚪ | 1 |

---

## Легенда статусов

| Иконка | Значение |
| :------: | :--------- |
| 🟢 | Активен, актуален |
| 🟡 | Требует обновления |
| 🔴 | Устарел / конфликтует |
| ⚪ | Черновик |

---

## Состояние 15 доменов

> Источник: `manifests/registry/domains-graph.yaml` (Протокол 016 САМ). Инфраструктурный поддомен `r2.blagorussia.ru` в таблицу контентных доменов не входит.

| # | Домен | Роль | Контур | Движок | Хостинг | Статус |
| :-: | :------ | :----- | :------: | :------: | :-------: | :------: |
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

> Known drift: `science.obrazslov.ru` и `r2.blagorussia.ru` соответствуют pending-интенту `manifests/registry/domain_rename_map.yaml` (`vacuum-condensate.obrazslov.ru` / `cdn.obrazslov.ru`). Применение — только через `rename_domains.py` после проверки DNS/301 (REG-020), не вручную (`do_not_apply_manually: true`).

---

## Состояние манифестов

> Источник: `manifests/registry/manifests.yaml`

| Манифест | Версия | Дата последней редакции | Статус | Протоколов |
| :--------- | :------: | :-----------------------: | :------: | :----------: |
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

> Источник: `manifests/registry/*.yaml` (operational-контур REG-). Отдельный слой от нормативных `.md`-манифестов; не смешивать 8 манифестов и 22 реестра.

| Метрика | Значение |
| :-------- | :--------: |
| Реестров YAML | 22 |
| Нормативных .md-манифестов | 8 |
| Контентных доменов | 15 |
| Инфраструктурных поддоменов | 1 |

Список реестров и их назначение — в [`README.md`](../README.md) и [`TASKS.md`](../TASKS.md) (раздел «Реестры manifests/registry»).

---

## Ключевые метрики

| Метрика | Значение | Цель |
| :-------- | :--------: | :----: |
| Доменов в экосистеме (контентных) | 15 | 15 |
| Манифестов всего | 8 | 8 |
| Манифестов активно | 7 | 7 |
| Манифестов черновиков | 1 | 1 |
| Машиночитаемых реестров | 22 | 22 |
| Успешность автообновления STATUS.md | interim (детерминированная генерация из реестров) | ≥99% после REG-014/017 |

---

## Активные риски

| # | Риск | Вероятность | Влияние | Митигация |
| :-: | :----- | :-----------: | :-------: | :---------- |
| 1 | Таксономия domains-graph пуста (INFRA-020) | Высокая | Средняя | Задача в реестре |
| 2 | Боевые scripts/.github/workflows/tests пусты; артефакты в archive | Высокая | Высокая | REG-016 / REG-017 / REG-018 (перенос после ревью) |
| 3 | update_status.py / sync_manifests.py читают отсутствующий реестр-источник (переехал в manifests/registry/) | Высокая | Высокая | REG-014 / REG-015 (пути -> manifests/registry, draft ⚪, динамические цели, docstring->факт) |
| 4 | domain_rename_map.yaml pending; science.obrazslov.ru / r2.blagorussia.ru как known drift | Средняя | Средняя | REG-020 (apply через rename_domains.py после проверки DNS) |
| 5 | Пустые tracked LICENSE-CODE / LICENSE-TEXT | Низкая | Низкая | REG-019 (решение Основателя) |
| 6 | Snapshot/unit-тесты ждут секцию «Состояние 14 доменов»; interim STATUS использует 15 | Высокая | Низкая | REG-018 (обновление тестов при переносе) |

**Последнее обновление**: 17.11.2026
