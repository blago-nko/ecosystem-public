"""Unit-тесты для scripts/registry/update_status.py (REG-014).

Runtime-валидация выполняется в CI (Python 3.12 + PyYAML из requirements.txt).
Локальный запуск невозможен в среде WindowsApps-stub Python.
"""
import re
import subprocess
import sys
from pathlib import Path


SCRIPT = 'scripts/registry/update_status.py'


def _run_script():
    return subprocess.run(
        [sys.executable, SCRIPT],
        capture_output=True,
        text=True,
        cwd=Path(__file__).parent.parent,
    )


def test_update_status_runs_without_error():
    """Скрипт update_status.py должен выполняться без ошибок."""
    result = _run_script()
    assert result.returncode == 0, f'STDERR: {result.stderr}'
    assert 'STATUS.md обновлён' in result.stdout


def test_status_md_exists_after_update():
    """После выполнения update_status.py docs/STATUS.md должен существовать."""
    _run_script()
    status_path = Path(__file__).parent.parent / 'docs' / 'STATUS.md'
    assert status_path.exists(), 'docs/STATUS.md не создан'
    content = status_path.read_text(encoding='utf-8')
    assert '# 📈 Статус документов' in content


def test_status_md_contains_required_sections():
    """docs/STATUS.md должен содержать обязательные секции; число доменов динамически."""
    _run_script()
    status_path = Path(__file__).parent.parent / 'docs' / 'STATUS.md'
    content = status_path.read_text(encoding='utf-8')

    required = [
        '## Текущее состояние',
        '## Состояние манифестов',
        '## Машиночитаемые реестры',
        '## Ключевые метрики',
        '## Активные риски',
    ]
    for section in required:
        assert section in content, f"Секция '{section}' отсутствует в STATUS.md"

    assert re.search(r'## Состояние \d+ доменов', content), \
        'Секция "Состояние N доменов" отсутствует или неверный формат'


def test_status_md_no_dead_source_link():
    """STATUS.md не должен ссылаться на отсутствующий docs/manifests.yaml."""
    _run_script()
    status_path = Path(__file__).parent.parent / 'docs' / 'STATUS.md'
    content = status_path.read_text(encoding='utf-8')

    assert 'docs/manifests.yaml' not in content, \
        'Мёртвая ссылка-источник docs/manifests.yaml присутствует в STATUS.md'

    assert 'manifests/registry/manifests.yaml' in content
    assert 'manifests/registry/domains-graph.yaml' in content
