# hybrid inheritance

class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name

class Gamer:

    def __init__(self, gname):
        self.gname = gname

class Student (Human, Gamer):

     def __init__(self, age, name, gname, study):
         self.study = study
         Human.__init__(self, age, name)
         Gamer.__init__(self, gname)


Vyanky = Student(21,'VJK', 'PUBG','Computer science')

print(Vyanky.gname)
print(Vyanky.study)
