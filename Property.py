class Confidential:

    def __init__(self, password):
        self._password = password

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        if new_password > 0 :
            self._password = new_password


    @password.deleter
    def password(self):
        del self._password


conf = Confidential('asdfghjkl')
print(conf.password)
Confidential.password = 'zxcvbnm'
print()
print(Confidential.password)

del Confidential.password
print(Confidential.password)

