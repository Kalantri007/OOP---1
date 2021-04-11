class Car :

    def gear(self):
        print ("Use your hands to change the gear")

    def top_speed(self):
        print("250 km?h")

    def fuel(self):
        print("CNG")

class Bike:

    def gear(self):
        print ("Use your foot to change the gear")

    def top_speed(self):
        print("150 km?h")

    def fuel(self):
        print("Petrol")


class Cycle:

    def gear(self):
        print("Use your finger to change the gear")

    def top_speed(self):
        print("50 km?h")

    def fuel(self):
        print("NONE")

c1 = Car()
b1 = Bike()
y1 = Cycle()

c1.gear()
b1.gear()
y1.gear()
print()
c1.fuel()
b1.fuel()
y1.fuel()
print()
c1.top_speed()
b1.top_speed()
y1.top_speed()

