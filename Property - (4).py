class Clg_Portal:

    def __init__(self):
        self.__name = ''

    @property
    # Getter method
    def name(self):
        return self.__name

    # Setter method
    @name.setter
    def name(self, val):
        self.__name = val

    # Deleter method
    @name.deleter
    def name(self):
        del self.__name


p = Clg_Portal();

p.name = 'VJK'

print(p.name)

del p.name

# for error check
#print(p.name)