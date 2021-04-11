class Emp:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Saurabh(Emp):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Emp):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

dev_1 = Saurabh('Pathu', 'Kalantri', 3000, 'Java')
dev_2 = Saurabh('Venku', 'Kalantri', 4000, 'Python')

mgr_1 = Manager('Shriniwas', 'Kalantri', 5000, [dev_1])

print(mgr_1.email)

mgr_1.add_emp(dev_2)

mgr_1.print_emps()
mgr_1.remove_emp(dev_2)

print('After remove function')

mgr_1.print_emps()