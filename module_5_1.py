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



h1 = House("ЖК Great Wall", 24)
h1.go_to(24)

h2 = House("Хрущевка", 5)
h2.go_to(10)

