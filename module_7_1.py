from pprint import pprint


class Product:

    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = round(float(weight), 1)
        self.category = str(category)

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}\n'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        text = file.read()
        file.close()
        return text

    def add(self, *products):
        file = open(self.__file_name, 'r+')
        for i in products:
            if str(i) in file:
                print(f'Продукт {i.name} уже есть в магазине')
            else:
                file.write(str(i))
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())