from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_print_mixin_product(capsys):
    Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    text = capsys.readouterr()
    assert text.out.strip() == "Product(Iphone 15, 512GB, Gray space, 210000.0, 8)"


def test_print_mixin_smartphone(capsys):
    Smartphone(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        31000.0,
        14,
        90.3,
        "Note 11",
        1024,
        "Синий",
    )
    text = capsys.readouterr()
    assert (
        text.out.strip()
        == "Smartphone(Xiaomi Redmi Note 11, 1024GB, Синий, 31000.0, 14)"
    )


def test_print_mixin_grass(capsys):
    LawnGrass(
        "Газонная трава 2",
        "Выносливая трава",
        450.0,
        15,
        "США",
        "5 дней",
        "Темно-зеленый",
    )
    text = capsys.readouterr()
    assert (
        text.out.strip() == "LawnGrass(Газонная трава 2, Выносливая трава, 450.0, 15)"
    )
