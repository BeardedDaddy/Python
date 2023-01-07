import datetime
import pytz

class Account:
    """ Simple account class with balance """

    """ This class creates a function for the account holders name and balance """

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transactions_list = []
        print("Account created for " + self.name)

    """ This class creates a function for amount after a deposit """
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()
            self.transactions_list.append((pytz.utc.localize(datetime.datetime.utcnow()), amount))

    """ This class creates a function for amount after a withdrawal """
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("You are over your acount balance of {}. Please enter a lesser amount? ".format(self.balance))
        self.show_balance()

    """ This class creates a function to show the balance """
    def show_balance(self):
        print("Balance is {}".format(self.balance))


    def show_transaction(self):
        for date, amount in self.transactions_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))

if __name__ == '__main__':
    grevy = Account("Grevy", 500000)
    grevy.show_balance()

    grevy.deposit(300000)
    # grevy.show_balance()
    grevy.withdraw(1000)
    # grevy.show_balance()

    grevy.withdraw(900000)
    grevy.show_transaction()
