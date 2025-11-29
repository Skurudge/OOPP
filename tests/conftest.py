import pytest

from src.category import Category
from src.product import Product


@pytest.fixture()
def product_one():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture()
def product_two():
    return Product("Iphone 16", "256GB, White", 210000.0, 12)


@pytest.fixture()
def category_one(product_one, product_two):
    return Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product_one, product_two],
    )
