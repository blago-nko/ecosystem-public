"""Snapshot-тесты для структуры docs/STATUS.md (REG-014 / REG-018).

Проверяет структуру и формат, не конкретные данные.
Число доменов ожидается динамически.
"""
import re
from pathlib import Path


def test_status_md_structure():
    """Проверка структуры docs/STATUS.md (обязательные секции и формат)."""
    status_path = Path(__file__).parent.parent.parent / 'docs' / 'STATUS.md'
    content = status_path.read_text(encoding='utf-8')

    assert content.startswith('# 📈 Статус документов'), 'Неверный заголовок'

    required_sections = [
        '## Текущее состояние',
        '## Легенда статусов',
        '## Состояние манифестов',
        '## Машиночитаемые реестры',
        '## Ключевые метрики',
        '## Активные риски',
    ]
    for section in required_sections:
        assert section in content, f"Секция '{section}' отсутствует"

    assert re.search(r'## Состояние \d+ доменов', content), \
        'Секция "Состояние N доменов" отсутствует или неверный формат'

    assert '| Манифест |' in content, 'Таблица манифестов отсутствует'

    timestamp_pattern = r'\d{2}\.\d{2}\.\d{4}'
    assert re.search(timestamp_pattern, content), \
        'Timestamp отсутствует или неверный формат; ожидается DD.MM.YYYY'

    assert 'docs/manifests.yaml' not in content, \
        'Мёртвая ссылка-источник docs/manifests.yaml присутствует'
