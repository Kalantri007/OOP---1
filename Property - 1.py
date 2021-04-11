class AC:

    def __init__(self, temp=0):
        self._temperature = temp

    @property
    # Getter method
    def temp(self):

        print("The value of the temperature is: ")
        return self._temperature

    # Setter method
    @temp.setter
    def temp(self, val):

        print("The value of the tempereture is set.")
        self._temperature = val


cel = AC();

cel.temp = 18

print(cel.temp)