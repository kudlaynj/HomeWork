class House:
    def __init__(self):
        self.numberOfFloors = 0
    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors.__add__(floors)
        print(floors)


my_house = House()
my_house.setNewNumberOfFloors(floors=1)
