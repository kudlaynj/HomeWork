class House:
    def __init__(self):
        self.numberOfFloors = 0
    def setNewNumberOfFloors(self):
        self.numberOfFloors += 1
        print(self.numberOfFloors)



my_house = House()
my_house.setNewNumberOfFloors()
