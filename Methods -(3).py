import datetime

class Holiday:

    def __init__ (self, first, last, pay):
        self.first = first
        self.last = last

    @staticmethod
    def Workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return "Lets play Pubg"
        return 'Lets do coding'

date = datetime.date(2021, 4, 3)

print(Holiday.Workday(date))
