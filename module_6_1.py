
class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

class Plant:
    edible = False

    def __init__(self, name):
        self.name = name

class Mammal(Animal, Plant):
    food = Plant

    def eat(self, food):
        if food.edible == True:
            self.fed = True
            print(f'{self.name} съел {food.name} и насытился')
            print(f'fed = {self.fed}')
        else:
            self.alive = False
            print(f'{self.name} съел {food.name} и умер')
            print(f'alive = {self.alive}')

class Predator(Animal, Plant):

    food = Plant

    def eat(self, food):
        if food.edible == True:
            self.fed = True
            print(f'{self.name} съел {food.name} и насытился')
            print(f'fed = {self.fed}')
        else:
            self.alive = False
            print(f'{self.name} съел {food.name} и умер')
            print(f'alive = {self.alive}')

class Flower(Plant):
    edible = False
class Fruit(Plant):
    edible = True


a1 = Predator("Волк")
a2 = Mammal("Козел")
p1 = Flower("Одуванчик")
p2 = Fruit("Апельсин")


print(a1.name)
print(p2.name)

print(a1.alive)
print(a2.fed)

a1.eat(p1)
a2.eat(p2)