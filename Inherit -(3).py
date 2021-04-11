class Car:
    def __init__(self, windows, doors, enginetype):
        self.windows = windows
        self.doors = doors
        self.enginetype = enginetype

    def drive(self):
        print("The Person drives the car")

car = Car(4,5,"diesel")
car.drive()

class Honda(Car):
    def __init__(self , windows, doors, enginetype, enable_ai):

        super().__init__(windows, doors, enginetype)
        self.enable_ai=enable_ai

    def selfdriving(self):
        print("Honda supports Self driving")

city = Honda(5, 5, "diesel", True)

city.selfdriving()