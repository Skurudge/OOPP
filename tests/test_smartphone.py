import pytest

from src.product import Product


def test_smartphone_init(smartphone_one):
    assert smartphone_one.name == "Samsung Galaxy S23 Ultra"
    assert smartphone_one.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone_one.price == 180000.0
    assert smartphone_one.quantity == 5
    assert smartphone_one.efficiency == 95.5
    assert smartphone_one.model == "S23 Ultra"
    assert smartphone_one.memory == 256
    assert smartphone_one.color == "Серый"


def test_smartphone_add(smartphone_one, smartphone_two):
    assert (
        smartphone_one + smartphone_two
        == "Общая стоимость товаров на складе: 1334000.0 руб."
    )


def test_smartphone_add_error(smartphone_one, grass_one):
    with pytest.raises(TypeError):
        Product.__add__(smartphone_one, grass_one)


def test_smartphone_add_error2(smartphone_one):
    with pytest.raises(TypeError):
        Product.__add__(smartphone_one, 10)
