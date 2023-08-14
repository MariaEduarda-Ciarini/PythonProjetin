class Account:
    def __init__(self, code):
        self._code = code
        self._balance = 0

    def deposit(self, value):
        self._balance += value

    def __str__(self):
        return "[>>Code {} Balance {}<<]".format(self._code, self._balance)


print(Account(54))


class Checking_Account(Account):
    def the_month_passes(self):
        self._balance -= 2


class SavingsAccount(Account):
    def the_month_passes(self):
        self._balance *= 1.01
        self._balance -= 3


account1 = Checking_Account(3)
account1.deposit(10000)
account1.the_month_passes()
print(account1)

account2 = SavingsAccount(4)
account2.deposit(1000)
account2.the_month_passes()
print(account2)

account1 = Checking_Account(3)
account1.deposit(10000)
account2 = SavingsAccount(4)
account2.deposit(1000)
acounts = [account1, account2]

for account in acounts:
    account.the_month_passes()
    print(account)