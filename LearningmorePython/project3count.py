class Count:
    def __init__(self, number, holder, balance, limit):
        print("Building object...{}".format(self))
        self.__number = number
        self.__holder = holder
        self.__balance = balance
        self.__limit = limit
    def extract(self):
        print("Holder's {} balance {}".format(self.__balance, self.__holder))

    def deposit(self, value):
        self.__balance += value
    def __can_withdraw_money(self, value_amout_withdraw):
         amount_available_withdraw = self.__balance + self.__limit
         return value_amout_withdraw <= amount_available_withdraw

    def check_out(self, value):
        if(self.__can_withdraw_money(value)):
            self.__balance -= value
        else:
            print("Withdrawal {} amount is exceeded".format(value))

    def transfer(self, value, destiny):
        self.check_out(value)
        destiny.deposit(value)

    def get_history(self):
        return self.__balance

    def get_holder(self):
        return self.__holder

    def get_extract(self):
        return self.__limit

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, limit):
        self.__limit = limit

    @staticmethod
    def bank_code():
        return "488"

    @staticmethod
    def banks_codes():
        return {'ITAÚ':'341', 'MSDW':'66', 'JPM':'488'}