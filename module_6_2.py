class Vehicle:
    __COLOR_VARIANTS = ["red", "black", "white", "blue"]

    def __init__(self, owner, model, engine_power, color):
        self.owner = str(owner)
        self.__model = str(model)
        self.__engine_power = int(engine_power)
        self.__color = str(color)

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner} \n')

    def set_color(self, new_color):
        new_color = str(new_color).lower()
        if new_color in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color} \n')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


car1 = Sedan('Екатерина', 'Toyota Crown', 500, 'red')
car1.print_info()

car1.set_color('pink')
car1.set_color('BLACk')
car1.print_info()

car1.owner = 'Марк'
car1.print_info()
