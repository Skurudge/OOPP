from src.order_product import OrderProduct


def test_print_order_product(capsys):
    OrderProduct("Iphone 15", "512GB, Gray space", 210000.0, 8, 3)
    text = capsys.readouterr()
    assert (
        text.out.strip() == "OrderProduct(Iphone 15, 512GB, Gray space, 210000.0, 8, 3)"
    )
