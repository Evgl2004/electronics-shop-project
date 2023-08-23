import pytest
from src.keyboard import Keyboard


@pytest.fixture
def coll_test_keyboard():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_str(coll_test_keyboard):
    assert str(coll_test_keyboard) == 'Dark Project KD87A'


def test_language(coll_test_keyboard):
    assert coll_test_keyboard.language == 'EN'


def test_change_lang(coll_test_keyboard):
    coll_test_keyboard.change_lang()
    assert coll_test_keyboard.language == 'RU'

    coll_test_keyboard.change_lang()
    assert coll_test_keyboard.language == 'EN'

    coll_test_keyboard.change_lang().change_lang()
    assert coll_test_keyboard.language == 'EN'


def test_setter_language(coll_test_keyboard):
    with pytest.raises(AttributeError):
        coll_test_keyboard.language = 'CH'
