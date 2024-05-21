class House:
    def __init__(self):
        self.name = 'Sweet home'


house = House()
house.numberOfFloors = 10

for i in range(1, 11):
    print('Текущий этаж равен ', i)

