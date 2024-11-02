import threading
import time

class Knight(threading.Thread):

    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = str(name)
        self.power = float(power)

    def run(self):
        print(f'{self.name}, на нас напали!')
        warriors = 100
        days = 0
        while warriors >= 0 + self.power:
            time.sleep(1)
            warriors -= self.power
            days += 1
            print(f'{self.name} сражается {days} дней..., осталось {warriors} воинов.\n')
        print(f'{self.name} одержал победу спустя {days} дней(дня)!\n')



first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()