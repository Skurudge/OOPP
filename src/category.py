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

    @property
    def products(self):
        """геттер для получения списка продуктов в нужном формате"""
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {product.price} руб., Остаток: {product.quantity} шт.\n"
        return product_str

    def add_product(self, new_product):
        """метод добавления new_product в список продуктов"""
        self.__products.append(new_product)

        Category.product_count += 1
