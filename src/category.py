from src.base_category import BaseCategory
from src.exceptions import ZeroQuantity
from src.product import Product


class Category(BaseCategory):
    """Класс для представления категории продукта"""

    name: str
    description: str
    __products: list
    product_count = 0
    category_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count = len(products)

    def __str__(self):
        total_quantity = 0
        for product in self.__products:
            total_quantity += product.quantity
        return f"{self.name}, Количество продуктов: {total_quantity} шт."

    @property
    def products(self):
        """геттер для получения списка продуктов в нужном формате"""
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"
        return product_str

    def add_product(self, new_product):
        """метод добавления new_product в список продуктов"""
        if isinstance(new_product, Product):
            try:
                if new_product.quantity == 0:
                    raise ZeroQuantity("Нельзя добавить продукт с нулевым количеством")
            except ZeroQuantity as e:
                print(str(e))
            else:
                self.__products.append(new_product)
                Category.product_count += 1
                print("Продукт добавлен успешно")
            finally:
                print("Обработка задачи добавления продукта завершена")
        else:
            raise TypeError

    def middle_price(self):
        try:
            middle = (
                sum([item.price for item in self.__products]) / Category.product_count
            )
            return round(middle, 1)
        except ZeroDivisionError:
            return 0.0
