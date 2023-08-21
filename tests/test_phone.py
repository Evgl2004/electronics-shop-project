import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def coll_test_item():
    test_item = Item("Смартфон", 10000, 20)
    Item.pay_rate = 0.8
    return test_item


@pytest.fixture
def coll_test_phone():
    test_phone = Phone("iPhone 14", 120_000, 5, 2)
    return test_phone


def test_str(coll_test_phone):
    assert str(coll_test_phone) == 'iPhone 14'


def test_repr(coll_test_phone):
    assert repr(coll_test_phone) == "Phone('iPhone 14', 120000, 5, 2)"


def test_number_sim_cards(coll_test_phone):
    assert coll_test_phone.number_of_sim == 2


def test_number_sim_cards_value_error(coll_test_phone):
    with pytest.raises(ValueError):
        coll_test_phone.number_of_sim = 0


def test_add(coll_test_item, coll_test_phone):
    assert coll_test_item + coll_test_phone == 25
    assert coll_test_phone + coll_test_phone == 10
