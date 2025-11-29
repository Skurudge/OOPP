import json
import os

from src.category import Category
from src.product import Product


def read_json_data(path: str) -> dict:
    my_path = os.path.abspath(path)
    with open(my_path, "r", encoding="UTF-8") as file:
        my_data = json.load(file)
        return my_data


def create_objects_from_json(data):
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))

    return categories


data_from_json = read_json_data("../data/products.json")
categories_data = create_objects_from_json(data_from_json)

print(categories_data)
print(categories_data[0].name)
print(categories_data[0].products)
