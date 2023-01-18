class Account:
    def __init__(self, balance, name):
        self.balance = balance
        self.name = name

    def credit(self, deposit):
        self.balance = self.balance + deposit

    def debit(self, withdrawal):
        self.balance = self.balance - withdrawal

    def get_balance(self):
        
