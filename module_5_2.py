class House:
    def __init__(self, name, numbers_of_floors):
        self.name = name
        self.number_of_floors = numbers_of_floors

    def go_to(self, new_floor):
        if int(new_floor) > int(self.number_of_floors) or (new_floor) < 1 or self.number_of_floors == 1:
            print("Перемещение на этот этаж невозможно")
        else:
            for i in range(1, int(new_floor)):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'

home1 = House('home1',12)
garage = House('garage', 1)
print(len(home1))
print(str(garage))