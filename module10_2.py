from datetime import datetime
from time import sleep
from threading import Thread

time_start = datetime.now()


class Knight(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.power = 100
        self.day = 1
        self.numb_war = 100

    def battle_start(self):
        print(f'{self.name}, на нас напали!')

    def battle_end(self):
        print(f'{self.name} одержал победу спустя {self.day-1} дней(дня)!')

    def run(self):
        self.battle_start()
        while self.numb_war > 0 and self.day <= 10:
            print(f'{self.name}, сражается {self.day} день(дня)..., осталось {self.numb_war} воинов.')
            self.power -= 10
            self.numb_war -= 10
            self.day += 1
            sleep(1)
        self.battle_end()


first_knight = Knight("Sir Melifaro")
second_knight = Knight("Sir Numinorih")

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

time_end = datetime.now()
time_res = time_end - time_start

print(f"Время битвы: {time_res}")
