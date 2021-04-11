class Intern:
    num = 0
    raise_per = 1.05

    def __init__ (self, first, last, pay):
        self.first = first
        self.last = last
        self.gmail = first + "." + last + "@gmail.com"
        self.pay = pay

        Intern.num += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise (self):
        self.pay = int(self.pay * self.raise_per)

    @classmethod
    def set_raise (cls, amount):
        cls.raise_per = amount

inter1 = Intern("Vyanky","Kalantri", 5000)
inter2 = Intern("Pathu", "Kalantri", 6000)

print("Number of Interns ", inter1.num)

print(inter1.fullname())
print(inter1.gmail)

inter1.apply_raise()
print("Raise before changes  ", inter1.raise_per)

Intern.set_raise(1.15)
print("Raise after changes  ", inter1.raise_per)



