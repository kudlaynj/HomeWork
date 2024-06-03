class Car:
    price = 1000000
    hp = 152

    def horse_powers(self):
        return self.hp


class Nissan(Car):
    price = 800000
    hp = 124

    def horse_powers(self):
        return self.hp


class Kia(Car):
    price = 1200000
    hp = 174

    def horse_powers(self):
        return self.hp


print("Автомобиль")
car_1 = Car()
car_1.horse_powers()

print("Nissan")
car_2 = Nissan()
car_2.horse_powers()

print("Kia")
car_3 = Kia()
car_3.horse_powers()
