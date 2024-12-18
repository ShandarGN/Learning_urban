# Импорт необходимых библиотек
import threading
import time
import random
import sys
# Шапка работы
print ('Created by',sys.version)
print ('Домашнее задание по теме "Блокировки и обработка ошибок"')
print ('Студент Анисимов Алексей Юрьевич')
print ('-'*20)
# Создание класса bank с атрибутами name, balance и lock (атрибут класса threading.Lock())
class bank():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.lock = threading.Lock()
# Описание методе deposit увеличивающего balance, принимает quantity - количество транзакций
    def deposit(self, quantity):
        print(f'Начальный баланс в банке {self.name}: {self.balance}.')
        while quantity > 0:
    # Проверка блокирования и размера баланса
            if self.lock.locked() and self.balance >= 500:
                self.lock.release()
                print('Счет разблокирован')
        # Генерация случайных транзакций и изменение баланса
            plus = random.randint(50, 450)
            self.balance += plus
            print(f'Пополнение: {plus}. Текущий баланс в банке {self.name}: {self.balance}.')
            quantity -= 1
            time.sleep(0.01)
# Описание метода take уменьшающего balance, принимает quantity - количество транзакций
    def take(self, quantity):
        print(f'Начальный баланс в банке {self.name}: {self.balance}.')
        max_quant = quantity
        while quantity > 0:
        # Генерация случайных транзакций и проверка блокировки
            minus = random.randint(50, 450)
            if self.lock.locked():
                print('Счет заблокирован, доступно только пополнение')
            else:
            # Проверка наличия средств для списания
                if minus <= self.balance:
                    self.balance -= minus
                    print(f'Снятие: {minus}. Текущий баланс в банке {self.name}: {self.balance}.')
                    quantity -= 1
                    time.sleep(0.01)
                else:
            # Блокировка при недостатке средств
                    self.lock.acquire()
                    print(f'Запрос № {max_quant - quantity + 1} на снятие {minus} отклонен средств {self.balance} недостаточно')
                    print('Счет заблокирован, доступно только пополнение')
                    break
# Создание объекта класса bank
test_bank = bank('Сбербанк', 1000)
# Создание потоков для метода dеposit и take с аргументом количество транзакций
thread_d = threading.Thread(target=test_bank.deposit, args = (80,))
thread_t = threading.Thread(target=test_bank.take, args = (80,))
# Запуск созданных потоков
thread_t.start()
thread_d.start()