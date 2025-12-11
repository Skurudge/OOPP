from src.category import Category


def test_category_init(category_one, product_one, product_two):
    assert category_one.name == "Телевизоры"
    assert (
        category_one.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert category_one.products == [product_one, product_two]
    assert len(category_one.products) == 2

    assert category_one.category_count == 1
    assert category_one.product_count == 2

    assert Category.category_count == 1
    assert Category.product_count == 2


def test_category_add_product(category_one, product_one, product_two, product_three):
    category_one.add_product(product_three)
    assert category_one.products == [product_one, product_two, product_three]
    assert len(category_one.products) == 3
