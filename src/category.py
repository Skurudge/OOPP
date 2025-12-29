from src.product import Product


class Category:
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
            self.__products.append(new_product)
            Category.product_count += 1
        else:
            raise TypeError
