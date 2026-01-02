class PrintMixin:

    def __init__(self):
        pass

    def __repr__(self):
        class_dict = vars(self)
        class_attribute_string = ", ".join(map(str, class_dict.values()))
        return f"{self.__class__.__name__}({class_attribute_string})"

    def print_attributes(self):
        print(repr(self))
