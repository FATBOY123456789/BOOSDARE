class Vehicle:
    def __init__(self,school_name,speed,mileage):
        self.school_name=school_name
        self.speed=speed
        self.mileage=mileage
    def display(self):
        print('The school ',self.school_name,'owns the bus, the speed of this bus is ',self.speed,'the mileage of the bus is ',self.mileage)
class Bus(Vehicle):
    def __init__(self, school_name, speed, mileage,totalfare):
        super().__init__(school_name, speed, mileage)
        self.totalfare=totalfare
    def display(self):
        super().display()
        print('The total fare of this bus is ',self.totalfare)
BOOS=Bus('School RKP',124,21,24500)
BOOS.display()