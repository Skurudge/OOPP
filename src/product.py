class Product:
    """Класс для представления продукта"""

    name: str
    description: str
    __price: float
    quantity: int

    products: list = []

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб., Остаток: {self.quantity} шт."

    def __add__(self, other):
        total_value = self.__price * self.quantity + other.__price * other.quantity
        return f"Общая стоимость товаров на складе: {total_value} руб."

    @classmethod
    def new_product(cls, product_dict):
        """класс-метод принимает параметры товара в словаре и возвращает созданный объект класса Product"""
        new_product = Product(**product_dict)
        return new_product

    @classmethod
    def update_or_add(cls, product, products):
        """класс-метод принимает продукт и проверяет его наличие в списке продуктов: в случае, если продукта нет в
        списке, то продукт добавляется в список. Если продукт есть в списке, то изменяются его цена и количество
        """
        found = False
        for prod in products:
            if prod.name == product.name:
                prod.price = max(prod.price, product.price)
                prod.quantity += product.quantity
                found = True
                break
        if not found:
            products.append(product)

        return products

    @property
    def price(self):
        """Определен геттер для приватной цены"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Определен сеттер для приватной цены"""
        if (new_price / self.__price) <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif 0 < (new_price / self.__price) < 1:
            request = input("Цену продукта снижаем? да(y)/нет(n): ")
            if request.lower() == "y":
                self.__price = new_price
        else:
            self.__price = new_price
