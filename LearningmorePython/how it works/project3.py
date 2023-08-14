def create_an_Account(number, holder, balance, limit):
    count = {"number": number, "holder": holder, "balance": balance, "limit": limit}
    return count

def deposit(count, value):
    count["balance"] += value

def check_out(count, value):
    if value <= count["balance"]:
        count["balance"] -= value
    else:
        print("The balance is not enough.")

def extract(count):
    print("Balance is {}".format(count["balance"]))
