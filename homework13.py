class Buiding:
    def __init__(self):
        self.numberOfFloors = int
        self.buildingType = str

    def __eq__(self, other):
        return self.numberOfFloors == other.buildingType


floors = Buiding()
floors2 = Buiding()

print(floors == floors2)
