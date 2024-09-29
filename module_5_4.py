class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, numbers_of_floors):
        self.name = name
        self.number_of_floors = numbers_of_floors

    def __del__(self):
        print(self.name, "снесен, но он останется в истории")
        self = None
        return self

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

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, other):
        if isinstance(other, int):
            self.number_of_floors = self.number_of_floors + other
            return self.number_of_floors

    def __iadd__(self, other):
        if isinstance(other, int):
            self.number_of_floors += other
            return self.number_of_floors

    def __radd__(self, other):
        if isinstance(other, int):
            self.number_of_floors = other + self.number_of_floors
            return self.number_of_floors

    def __sub__(self, other):
        if isinstance(other, int):
            self.number_of_floors = self.number_of_floors - other
            return self.number_of_floors

    def __mul__(self, other):
        if isinstance(other, int):
            self.number_of_floors = self.number_of_floors * other
            return self.number_of_floors

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

del h2
del h3


print(House.houses_history)
