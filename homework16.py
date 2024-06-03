class Vehicle:
    vehicle_type = "none"


class Car:
    price = 1000000

    def horse_powers(self):
        return

class Nissan(Car, Vehicle):
    price = 1200000
    vehicle_type = "yes"

    def __init__(self):
        self.hp = int

    def horse_powers(self):
        self.hp = 154


car_1 = Nissan()
print(car_1.vehicle_type)
print(car_1.price)