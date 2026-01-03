from src.base_category import BaseCategory
from src.exceptions import ZeroQuantity
from src.print_mixin import PrintMixin


class OrderProduct(BaseCategory, PrintMixin):

    def __init__(self, name, description, price, quantity_stock, quantity_order):
        super().__init__()
        self.name = name
        self.description = description
        self.price = price
        self.quantity_stock = quantity_stock
        try:
            if quantity_order == 0:
                raise ZeroQuantity(
                    "Невозможно создать заказ с нулевым количеством товара"
                )
        except ZeroQuantity as e:
            print(str(e))
        else:
            self.quantity_order = quantity_order
            print("Заказ создан успешно")
            self.print_attributes()
        finally:
            print("Задача создания заказа завершена")

    @property
    def total_value(self):
        return self.price * self.quantity_order

    def __str__(self):
        return f"Продукт {self.name}. Продано в заказе {self.quantity_order} шт. на сумму {self.total_value} руб."
