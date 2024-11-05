import threading
from random import randint
import time


class Bank:
    def __init__(self, balance=0):
        self.balance = int(balance)
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            time.sleep(0.001)
            rand = randint(50, 500)
            with self.lock:
                if self.balance + rand > 500:
                    pass
                else:
                    self.balance += rand
                    print(f'Пополнение: {rand}. Баланс: {self.balance}')

    def take(self):
        for i in range(100):
            time.sleep(0.001)
            rand = randint(50, 500)
            with self.lock:
                print(f'Запрос на {rand}, при текущем балансе - {self.balance}')
                if self.balance - rand >= 0:
                    self.balance -= rand
                    print(f'Снятие: {rand}. Баланс: {self.balance}')
                else:
                    print(f'Запрос отклонён, недостаточно средств')

bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')
