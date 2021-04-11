
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    @property
    def gmail(self):
        if self.fname==None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@gmail.com"

    @gmail.setter
    def gmail(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[0]

    @gmail.deleter
    def gmail(self):
        self.fname = None
        self.lname = None


obj = Employee("Vyaky", "Kalantri")

print(obj.gmail)

obj.fname = "Vyankatesh"

print(obj.gmail)
obj.gmail = "Prathamesh@gmail.com"
print(obj.fname)

del obj.gmail
print(obj.gmail)
obj.gmail = "Vyanky.kalantri22@gmail.com"
print(obj.gmail)

