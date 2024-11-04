import threading
import time
import random
from threading import Lock


class Bank:
    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            i = random.randint(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

            self.balance += i
            print(f'Пополнение: {i}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for j in range(100):
            j = random.randint(50, 500)
            print(f'Запрос на {j}')
            if j <= self.balance:
                self.balance -= j
                print(f"Снятие: {j}. Баланс: {self.balance}.")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')