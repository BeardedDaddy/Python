class Account:
    """ Simple account class with balance """

    """ This class creates a function for the account holders name and balance """

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print("Account create for " + self.name)

    """ This class creates a function for amount after a deposit """
    def deposit(self,amount):
        if amount >0:
            self.balance += amount

    """ This class creates a function for amount after a withdrawal """
    def withdraw(self, amount):
        if amount >0:
            self.balance -= amount

    """ This class creates a function to show the balance """
    def show_balance(self):
        print("Balance is {}".format(self.balance))
