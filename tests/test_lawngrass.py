import pytest

from src.product import Product


def test_grass_init(grass_one):
    assert grass_one.name == "Газонная трава 2"
    assert grass_one.description == "Выносливая трава"
    assert grass_one.price == 450.0
    assert grass_one.quantity == 15
    assert grass_one.country == "США"
    assert grass_one.germination_period == "5 дней"
    assert grass_one.color == "Темно-зеленый"


def test_smartphone_add(grass_one, grass_two):
    assert grass_one + grass_two == "Общая стоимость товаров на складе: 16750.0 руб."


def test_smartphone_add_error(grass_two, smartphone_one):
    with pytest.raises(TypeError):
        Product.__add__(grass_two, smartphone_one)


def test_smartphone_add_error2(grass_one):
    with pytest.raises(TypeError):
        Product.__add__(grass_one, "j")
