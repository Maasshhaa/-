from queue import Queue
import time
import threading
from random import randint

class Table:
    def __init__(self, number, occupied=None):
        self.number = number
        self.occupied = occupied


class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        rand_time = randint(3, 10)
        time.sleep(rand_time)


class Cafe:

    def __init__(self, *tables, queue = Queue()):
        self.tables = tables
        self.queue = queue

    def guest_arrival(self, *guests):
        self.guests = guests
        for i in range(len(guests)):
            try:
                if self.tables[i].occupied is None:
                    self.tables[i].occupied = guests[i].name
                    guests[i].start()
                    print(f'{guests[i].name} сел(-а) за стол номер {self.tables[i].number}')
            except:
                self.queue.put(guests[i])
                print(f'{guests[i].name} в очереди')

    def discuss_guests(self):
        while not all(table.occupied == None for table in self.tables):
            for i in range(len(self.tables)):
                if tables[i].occupied != None and not self.guests[i].is_alive():
                    print(f'{tables[i].occupied} покушал(-а) и ушёл(ушла)')
                    print(f'стол номер {tables[i].number} свободен')
                    tables[i].occupied = None
                if tables[i].occupied is None:
                    new_guests = self.queue.get()
                    tables[i].occupied = new_guests.name
                    print(f'{tables[i].occupied} вышел(-ла) из очереди и сел(-а) за стол номер {tables[i].number}')
                    new_guests.start()
                    rand_time = randint(3, 10)
                    time.sleep(rand_time)


tables = [Table(number) for number in range(1, 6)]
# self.queue.empty() or
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman','Vitoria', 'Nikita', 'Galina',
                'Pavel', 'Ilya', 'Alexandra']

guests = [Guest(name) for name in guests_names]

cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()