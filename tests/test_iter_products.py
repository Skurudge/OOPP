def test_iter_products(iterator_one):
    assert iterator_one.index == 0
    assert next(iterator_one) == "Iphone 15, 210000.0 руб., Остаток: 8 шт."
    assert next(iterator_one) == "Iphone 16, 210000.0 руб., Остаток: 12 шт."
