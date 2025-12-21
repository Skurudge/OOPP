import pytest

from src.category import Category


def test_category_init(category_one, product_one, product_two):
    assert category_one.name == "Телевизоры"
    assert (
        category_one.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert category_one.products == (
        "Iphone 15, 210000.0 руб., Остаток: 8 шт.\n"
        "Iphone 16, 210000.0 руб., Остаток: 12 шт.\n"
    )

    assert category_one.category_count == 1
    assert category_one.product_count == 2

    assert Category.category_count == 1
    assert Category.product_count == 2


def test_category_add_product(category_one, product_one, product_two, product_three):
    category_one.add_product(product_three)
    assert category_one.products == (
        "Iphone 15, 210000.0 руб., Остаток: 8 шт.\n"
        "Iphone 16, 210000.0 руб., Остаток: 12 шт.\n"
        "Iphone 17, 240000.0 руб., Остаток: 1 шт.\n"
    )
    assert Category.product_count == 3


def test_str_category(category_one):
    assert str(category_one) == "Телевизоры, Количество продуктов: 20 шт."


def test_category_add_product_error(category_one):
    with pytest.raises(TypeError):
        category_one.add_product("Not a product")
