from unittest.mock import patch

import pytest

from src.product import Product


def test_product_init_product_one(product_one):
    assert product_one.name == "Iphone 15"
    assert product_one.description == "512GB, Gray space"
    assert product_one.price == 210000.0
    assert product_one.quantity == 8


def test_product_init_product_two(product_two):
    assert product_two.name == "Iphone 16"
    assert product_two.description == "256GB, White"
    assert product_two.price == 210000.0
    assert product_two.quantity == 12


def test_price_negative(product_one):
    product_one.price = -100000.0
    assert product_one.price == 210000.0


def test_price_increase(product_one):
    product_one.price = 350000.0
    assert product_one.price == 350000.0


@patch("builtins.input", return_value="y")
def test_price_decrease_yes(product_one):
    product_one.price = 150000.0
    assert product_one.price == 150000.0


def test_str_product(product_one):
    assert str(product_one) == "Iphone 15, 210000.0 руб., Остаток: 8 шт."


def test_add_product(product_one, product_two):
    assert (
        product_one + product_two == "Общая стоимость товаров на складе: 4200000.0 руб."
    )


def test_product_zero_quantity():
    with pytest.raises(
        ValueError, match="Товар с нулевым количеством не может быть добавлен"
    ):
        Product("Iphone 15", "512GB, Gray space", 210000.0, 0)
