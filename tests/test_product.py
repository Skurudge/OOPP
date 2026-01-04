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


def test_product_from_dict(product_sample_dict):
    product = Product.new_product(product_sample_dict)
    assert str(product) == "Samsung Galaxy S23 Ultra, 180000.0 руб., Остаток: 5 шт."


def test_update_or_add__update():
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    product4 = Product("Iphone 15", "512GB, Gray space", 240000.0, 12)

    product_list = Product.update_or_add(product4, [product2, product3])

    assert len(product_list) == 2
    assert str(product_list[0]) == "Iphone 15, 240000.0 руб., Остаток: 20 шт."
    assert str(product_list[1]) == "Xiaomi Redmi Note 11, 31000.0 руб., Остаток: 14 шт."


def test_update_or_add__add():
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    product4 = Product("Iphone 17", "512GB, Black space", 250000.0, 1)

    product_list = Product.update_or_add(product4, [product2, product3])

    assert len(product_list) == 3
    assert str(product_list[0]) == "Iphone 15, 210000.0 руб., Остаток: 8 шт."
    assert str(product_list[1]) == "Xiaomi Redmi Note 11, 31000.0 руб., Остаток: 14 шт."
    assert str(product_list[2]) == "Iphone 17, 250000.0 руб., Остаток: 1 шт."
