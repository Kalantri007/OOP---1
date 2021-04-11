class Trace:

    def __init__(self, x=0 , y=0):
        self.x = x
        self.y = y

        @property
        def loc(self):
            print(self.x, self.y)

        @loc.setter
        def loc(self, loc):
            self.x, self.y = loc

        @loc.deleter
        def loc(self):
            self.x = self.y = 0

        def origin(self):
            self.x = self.y = 0

        def left (self):
            self.x -= 1

        def right (self):
            self.x += 1

        def up (self):
            self.y -= 1

        def down(self):
            self.y += 1

t1 = Trace()

t1.loc = [2,3]
print(t1.loc)
print()
print(t1.loc)
