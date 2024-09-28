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

h1 = House('home1',12)
h2 = House('garage', 1)

print(h1)
print(h2)
print(h1 == h2)

h1 = h1 + 10
print(h1)
print(h1 == h2)

h1 += 10
print(h1)

h2 = 10 + h2
print(h2)

h2 = 10 - h2
print(h2)

h2 = 10 * h2
print(h2)

print(h1 > h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 != h2)

