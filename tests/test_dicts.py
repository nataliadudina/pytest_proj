import pytest

from utils.dicts import get_val


def test_dicts():
    assert get_val({'one': 1, 'two': 2, 'three': 3}, 'two', default='git') == 2
    assert get_val({'one': 1, 'two': 2, 'three': 3}, 'five', default='git') == 'git'
    assert get_val({}, 'two', default='git') == 'git'
    assert get_val({}, 'two', default='python') == 'python'
