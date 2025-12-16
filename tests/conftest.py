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
def product_three():
    return Product("Iphone 17", "256GB, Titan", 240000.0, 1)


@pytest.fixture()
def category_one(product_one, product_two):
    return Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product_one, product_two],
    )


@pytest.fixture()
def json_data_products():
    return [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации, но и удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                },
                {
                    "name": "Iphone 15",
                    "description": "512GB, Gray space",
                    "price": 210000.0,
                    "quantity": 8,
                },
            ],
        }
    ]
