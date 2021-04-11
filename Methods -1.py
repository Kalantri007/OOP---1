import math

class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi

    @classmethod
    def cheese_burst(cls):
        print('cheese_4, myonese')
        return cls(['cheese_4', 'myonese'])

p = Pizza(5, ['cheez', 'onion'])

print(p.area())
print(Pizza.circle_area(5))
print('>>>>>>>>>>>>>>>>>>>')
print(Pizza.cheese_burst())
