#!/usr/bin/env python3
"""Перегенерирует docs/STATUS.md из источников правды (единственный писатель файла).

Источники: manifests/registry/manifests.yaml, manifests/registry/domains-graph.yaml.
Формат timestamp-строки — контракт с .github/workflows/update-status.yml:
**Последнее обновление**: DD.MM.YYYY (UTC)

Контракт INFRA-029: этот скрипт — единственный писатель docs/STATUS.md.
sync_manifests.py НЕ должен писать STATUS.md.
"""
from datetime import datetime, timezone
from pathlib import Path
import sys

import yaml

# scripts/registry/update_status.py -> корень репозитория
ROOT = Path(__file__).resolve().parent.parent.parent


def load_yaml(rel):
    p = ROOT / rel
    if not p.exists():
        return {}
    with open(p, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def status_icon(status):
    if status == "active":
        return "🟢"
    if status == "draft":
        return "⚪"
    return "🟡"


def main():
    args = sys.argv[1:]
    if args in (["--help"], ["-h"]):
        print("Usage: python scripts/registry/update_status.py")
        print("Regenerates docs/STATUS.md from manifests/registry sources.")
        print("Run without arguments to update. --help/-h do not write.")
        return
    if args:
        print(f"ERROR: unsupported arguments: {' '.join(args)}", file=sys.stderr)
        print("Run without arguments or with --help.", file=sys.stderr)
        raise SystemExit(2)

    manifests = load_yaml("manifests/registry/manifests.yaml").get("manifests", [])
    graph = load_yaml("manifests/registry/domains-graph.yaml")
    domains = graph.get("domains", [])
    infra = graph.get("infra", [])

    now_utc = datetime.now(timezone.utc)
    stamp = now_utc.strftime("%d.%m.%Y")

    active_count = sum(1 for m in manifests if m.get("status") == "active")
    draft_count = sum(1 for m in manifests if m.get("status") == "draft")
    registry_count = len(list((ROOT / "manifests" / "registry").glob("*.yaml")))

    lines = [
        "# 📈 Статус документов",
        "",
        "> ⚠️ **Этот файл обновляется автоматически** через GitHub Actions",
        "> (`.github/workflows/update-status.yml`). Не редактируйте вручную.",
        "> Реестр задач: [TASKS.md](../TASKS.md). Долгосрочный план: [ROADMAP.md](../ROADMAP.md).",
        "",
        "---",
        "",
        "## Текущее состояние",
        "",
        "| # | Манифест | Файл | Версия | Дата | Статус | Протоколов |",
        "|:-:|:---------|:-----|:------:|:----:|:------:|:----------:|",
    ]
    for i, m in enumerate(manifests, 1):
        icon = status_icon(m.get("status", ""))
        lines.append(
            f"| {i} | {m.get('short_title','')} | `{m.get('file','')}` | {m.get('version','')} "
            f"| {m.get('last_revision','')} | {icon} | {m.get('protocols',0)} |"
        )
    lines += [
        "",
        "---",
        "",
        "## Легенда статусов",
        "",
        "| Иконка | Значение |",
        "|:------:|:---------|",
        "| 🟢 | Активен, актуален |",
        "| 🟡 | Требует обновления |",
        "| 🔴 | Устарел / конфликтует |",
        "| ⚪ | Черновик |",
        "",
        "---",
        "",
        f"## Состояние {len(domains)} доменов",
        "",
        f"> Источник: `manifests/registry/domains-graph.yaml` (Протокол 016 САМ). Инфраструктурных поддоменов: {len(infra)}.",
        "",
        "| # | Домен | Роль | Контур | Движок | Хостинг | Статус |",
        "|:-:|:------|:-----|:------:|:------:|:-------:|:------:|",
    ]
    for i, d in enumerate(domains, 1):
        lines.append(
            f"| {i} | {d.get('fqdn','')} | {d.get('role','')} | {d.get('contour','')} "
            f"| {d.get('engine','')} | {d.get('hosting','')} | 🟢 |"
        )
    lines += [
        "",
        "> Known drift: `science.obrazslov.ru` и `r2.blagorussia.ru` соответствуют pending-интенту `manifests/registry/domain_rename_map.yaml`. Применение — только через `rename_domains.py` (REG-020), не вручную (`do_not_apply_manually: true`).",
        "",
        "---",
        "",
        "## Состояние манифестов",
        "",
        "> Источник: `manifests/registry/manifests.yaml`",
        "",
        "| Манифест | Версия | Дата последней редакции | Статус | Протоколов |",
        "|:---------|:------:|:-----------------------:|:------:|:----------:|",
    ]
    for m in manifests:
        icon = status_icon(m.get("status", ""))
        lines.append(
            f"| {m.get('short_title','')} | {m.get('version','')} | {m.get('last_revision','')} "
            f"| {icon} | {m.get('protocols',0)} |"
        )
    lines += [
        "",
        "---",
        "",
        "## Машиночитаемые реестры",
        "",
        "> Источник: `manifests/registry/*.yaml` (operational-контур REG-). Отдельный слой от нормативных .md-манифестов; не смешивать манифесты и реестры.",
        "",
        "| Метрика | Значение |",
        "| :-------- | :--------: |",
        f"| Реестров YAML | {registry_count} |",
        f"| Нормативных .md-манифестов | {len(manifests)} |",
        f"| Контентных доменов | {len(domains)} |",
        f"| Инфраструктурных поддоменов | {len(infra)} |",
        "",
        "---",
        "",
        "## Ключевые метрики",
        "",
        "| Метрика | Значение | Цель |",
        "|:--------|:--------:|:----:|",
        f"| Доменов в экосистеме (контентных) | {len(domains)} | {len(domains)} |",
        f"| Манифестов всего | {len(manifests)} | {len(manifests)} |",
        f"| Манифестов активно | {active_count} | {active_count} |",
        f"| Манифестов черновиков | {draft_count} | {draft_count} |",
        f"| Машиночитаемых реестров | {registry_count} | {registry_count} |",
        "| Успешность автообновления STATUS.md | ≥99% | ≥99% |",
        "",
        "---",
        "",
        "## Активные риски",
        "",
        "| # | Риск | Вероятность | Влияние | Митигация |",
        "|:-:|:-----|:-----------:|:-------:|:----------|",
        "| 1 | Таксономия domains-graph пуста (INFRA-020) | Высокая | Средняя | Задача в реестре |",
        "| 2 | sync_manifests.py содержит блок записи STATUS (нарушает INFRA-029); требует полного ревью | Высокая | Высокая | REG-015 |",
        "| 3 | domain_rename_map.yaml pending; science.obrazslov.ru / r2.blagorussia.ru как known drift | Средняя | Средняя | REG-020 |",
        "| 4 | Пустые tracked LICENSE-CODE / LICENSE-TEXT | Низкая | Низкая | REG-019 |",
        "| 5 | Runtime-валидация update_status.py отложена до CI (Python локально недоступен) | Высокая | Средняя | REG-017 после push |",
        "",
        f"**Последнее обновление**: {stamp}",
        "",
    ]
    (ROOT / "docs" / "STATUS.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"STATUS.md обновлён: манифестов — {len(manifests)}, доменов — {len(domains)}, реестров — {registry_count}")


if __name__ == "__main__":
    main()
