class Product:

    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)


    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'



    def get_products(self):
        file = open(self.__file_name, 'r')
        file_read = file.read()
        file.close()
        return file_read


    def add(self, *products):
        for i in products:
            g_prod = self.get_products()
            _file = open(self.__file_name, 'a')
            _file.write(f'{i}\n')
            _file.close()
            if i.name in g_prod:
                print(f'Продукт {i.name} уже есть в магазине')
            else:
                continue




s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())