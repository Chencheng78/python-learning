# this task is a way to show how to define a class


class Building:
    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.south = south
        self.west = west
        self.width_WE = width_WE
        self.width_NS = width_NS
        self.height = height

    def corners(self):
        direction = ["north-west", "north-east", "south-west", "south-east"]
        axis = [[self.south + self.width_NS, self.west],[self.south + self.width_NS,self.west + self.width_WE],[self.south,self.west],[self.south, self.west + self.width_WE]]
        return dict(zip(direction,axis))

    def area(self):
        return self.width_NS * self.width_WE

    def volume(self):
        return self.width_NS * self.width_WE * self.height

    def __repr__(self):
        return 'Building(%g, %g, %g, %g, %g)' %(self.south, self.west,self.width_WE, self.width_NS, self.height)

print(Building(1, 2, 2, 2).corners())
print(Building(1, 2.5, 4.2, 1.25).area())
print(str(Building(0, 0, 10.5, 2.546)))