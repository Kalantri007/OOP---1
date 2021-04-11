class MethodTypes:

    name = "Vyanky"

    def instanceMethod(self):
        # Creates an instance atribute through keyword self
        self.lastname = "Kalantri"
        print(self.name)
        print(self.lastname)

    @classmethod
    def classMethod(cls):
        # Access a class atribute through keyword cls
        cls.name = "Pathu"
        print(cls.name)

    @staticmethod
    def staticMethod():
        print("static method")

# Creates an instance of the class
m = MethodTypes()
# Calls instance method
m.instanceMethod()
# Calls class method
MethodTypes.classMethod()
# Calls static
MethodTypes.staticMethod()
