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

home1 = House('home1',12)
garage = House('garage', 1)
home1.go_to(6)
garage.go_to(1)