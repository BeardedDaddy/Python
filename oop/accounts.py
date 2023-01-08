import datetime
import pytz

class Account:
    """ Simple account class with balance """

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    """ This class creates a function for the account holders name and balance """

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transaction_list = [(Account._current_time(), balance)]
        print("Account created for " + self._name)
        self.show_balance()

    """ This class creates a function for amount after a deposit """
    def deposit(self,amount):
        if amount >0:
            self.__balance += amount
            self.show_balance()
            self._transaction_list.append((pytz.utc.localize(datetime.datetime.utcnow()), amount))

    """ This class creates a function for amount after a withdrawal """
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("You are over your acount balance of {}. Please enter a lesser amount? ".format(self.__balance))
        self.show_balance()

    """ This class creates a function to show the balance """
    def show_balance(self):
        print("Balance is {}".format(self.__balance))

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount >0:
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
    grevy.show_transactions()

    mia = Account("Mia", 300000)
    mia.balance = 200
    mia.deposit(10000)
    mia.withdraw(500)
    mia.show_transactions()
    print(mia.__dict__)
    mia._Account__balance = 40
    mia.show_balance()
    