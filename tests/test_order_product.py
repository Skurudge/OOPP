from src.order_product import OrderProduct


def test_print_order_product(capsys):
    OrderProduct("Iphone 15", "512GB, Gray space", 210000.0, 8, 3)
    text = capsys.readouterr()
    assert text.out.strip().split("\n")[-3] == "Заказ создан успешно"
    assert (
        text.out.strip().split("\n")[-2]
        == "OrderProduct(Iphone 15, 512GB, Gray space, 210000.0, 8, 3)"
    )
    assert text.out.strip().split("\n")[-1] == "Задача создания заказа завершена"


def test_order_product_zero_quantity(capsys):
    OrderProduct("Iphone 15", "512GB, Gray space", 210000.0, 8, 0)
    text = capsys.readouterr()
    assert (
        text.out.strip().split("\n")[-2]
        == "Невозможно создать заказ с нулевым количеством товара"
    )
    assert text.out.strip().split("\n")[-1] == "Задача создания заказа завершена"
