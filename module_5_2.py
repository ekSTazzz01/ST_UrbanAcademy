class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor):
        for floor in range(1, new_floor + 1):
            if floor > self.number_of_floors or floor < 1:
                print('Такого этажа не существует')
                break
            else:
                print(floor)


    def __len__(self):
        return self.number_of_floors


    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'


h1 = House("ЖК Great Wall", 24)
# h1.go_to(24)

h2 = House("Хрущевка", 5)
# h2.go_to(10)

print(len(h1))
print(len(h2))
print(str(h1))
print(str(h2))