import pytest

from utils.dicts import get_val


@pytest.mark.parametrize('collection, key, default, expected', [
    ({'one': 1, 'two': 2, 'three': 3}, 'two', 'git', 2),
    ({'one': 1, 'two': 2, 'three': 3}, 'five', 'git', 'git'),
    ({}, 'two', 'git', 'git'),
    ({}, 'two', 'python', 'python')
])
def test_dicts(collection, key, default, expected):
    assert get_val(collection, key, default) == expected
