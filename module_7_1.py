from pprint import pprint


class Product:  # продукт
    def __init__(self, name, weight, category):  # название,  вес, категория
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return f'название: "{self.name}", вес: "{self.weight}", категория:  "{self.category}"'


class Shop():  # магазин
    __file_name = 'products.txt'
    products = []

    def get_products(self):  # получить_продукты
        file = open(self.__file_name, 'r')
        products = file.read()
        file.close()
        return products

    def add(self, *products):  # добавление продукта
        current_products = self.get_products()
        file_n = open(self.__file_name, 'w', encoding='utf-8')
        for i in products:
            if i.name not in current_products:
                file_n.write(f"{i}\n")
                current_products += str(i)+'\n'
            else:
                print(f'Продукт {i} уже есть в магазине')
        file_n.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

print(s1._Shop__file_name)