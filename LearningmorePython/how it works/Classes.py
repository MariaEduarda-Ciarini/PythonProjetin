class SalaryAccount:
    def __init__(self, code):
        self._code = code
        self._balance = 0

    def deposit(self, value):
        self._balance += value

    def __str__(self):
        return "[>>Code {} Balance {}<<]".format(self._code, self._balance)


acount3 = SalaryAccount(5)
print(acount3)

acount4 = SalaryAccount(5)
print(acount4)

print(acount3 == acount4)


class SalaryAccount:
    def __init__(self, code):
        self._code = code
        self._balance = 0

    def deposit(self, value):
        self._balance += value

    def __str__(self):
        return "[>>Code {} Balance {}<<]".format(self._code, self._balance)

    def __eq__(self, other):
        return self._code == other._code and self._balance == other._code


acount3 = SalaryAccount(5)
print(acount3)

acount4 = SalaryAccount(5)
print(acount4)

print(acount3 == acount4)

print(acount3 in [acount4])
print(acount4 in [acount3])

acount3.deposit(150)
print(acount3 == acount4)


class SalaryAccount:
    def __init__(self, code):
        self._code = code
        self._balance = 0

    def deposit(self, value):
        self._balance += value

    def __str__(self):
        return "[>>Code {} Balance {}<<]".format(self._code, self._balance)

    def __eq__(self, other):
        if type(other) != SalaryAccount:
            return False

        return self._code == other._code and self._balance == other._code

acount3 = SalaryAccount(33)


def Checking_Account(param):
    pass


acount4 = Checking_Account(33)
print(acount3 == acount4)
