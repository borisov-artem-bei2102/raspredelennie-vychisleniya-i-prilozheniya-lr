import threading
import random
import time


class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.move = 1

    def attack(self, other):
        while True:
            if self.health <= 0:
                return
            other.health -= 20
            print(f'Ход {self.move}. {self.name} атаковал, у {other.name} осталось {other.health} очков здоровья')
            if other.health <= 0:
                print(f'{self.name} одержал победу!\n')
                return
            self.move += 1
            time.sleep(random.randint(1, 5))


warrior1 = Warrior('Дмитрий')
warrior2 = Warrior('Олег')

thread1 = threading.Thread(target=warrior1.attack, args=(warrior2,))
thread2 = threading.Thread(target=warrior2.attack, args=(warrior1,))

thread1.start()
thread2.start()
