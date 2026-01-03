import pytest

from src.category import Category
from src.product import Product


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


def test_middle_price_zero():
    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    assert category_empty.middle_price() == 0.0


def test_middle_price(category_one):
    assert category_one.middle_price() == 210000.0


def test_add_product(capsys):
    new_product = Product("Iphone 15", "512GB, Gray space", 210000.0, 4)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    category1 = Category("Смартфоны", "Категория смартфонов", [product2, product3])
    category1.add_product(new_product)
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-2] == "Продукт добавлен успешно"
    assert (
        message.out.strip().split("\n")[-1]
        == "Обработка задачи добавления продукта завершена"
    )
