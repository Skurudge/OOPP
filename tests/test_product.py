def test_product_init_01(product_one):
    assert product_one.name == "Iphone 15"
    assert product_one.description == "512GB, Gray space"
    assert product_one.price == 210000.0
    assert product_one.quantity == 8


def test_product_init_02(product_two):
    assert product_two.name == "Iphone 16"
    assert product_two.description == "256GB, White"
    assert product_two.price == 210000.0
    assert product_two.quantity == 12
