class ProductsIterator:
    def __init__(self, category_object):
        self.category = category_object
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.category.products.split("\n")):
            product = self.category.products.split("\n")[self.index]
            self.index += 1
            return product.strip()
        else:
            raise StopIteration
