import sqlite3
import datetime
import pytz

db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)
db.execute("CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL)")  # noqa: E501
db.execute("CREATE TABLE IF NOT EXISTS history (time TIMESTAMP NOT NULL,"
           " account TEXT NOT NULL, amount INTEGER NOT NULL, PRIMARY KEY (time, account))")  # noqa: E501
db.execute("CREATE VIEW IF NOT EXISTS localhistory AS"
           " SELECT strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime') AS localtime,"  # noqa: E501
           " history.account, history.amount FROM history ORDER BY history.time")  # noqa


class Account(object):

    @staticmethod
    def _current_time():
        return pytz.utc.localize(datetime.datetime.utcnow())

    def __init__(self, name: str, opening_balance: int = 0):
        cursor = db.execute("SELECT name, balance FROM accounts WHERE (name = ?)", (name,))  # noqa: E501
        row = cursor.fetchone()

        if row:
            self.name, self._balance = row
            print("Retrieved record for {}. ".format(self.name), end='')
        else:
            self.name = name
            self._balance = opening_balance
            cursor.execute("INSERT INTO accounts VALUES(?, ?)", (name, opening_balance))  # noqa
            cursor.connection.commit()
            print("Account created for {}. ".format(self.name), end='')
        self.show_balance()

    def _save_update(self, amount):
        new_balance = self._balance + amount
        deposit_time = Account._current_time()

        try:
            db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))  # noqa
            db.execute("INSERT INTO history VALUES(?, ?, ?)", (deposit_time, self.name, amount))  # noqa

        except sqlite3.Error:
            # db.rollback()
            pass
        else:
            db.commit()
            self._balance = new_balance

        self._balance = new_balance

    def _save_update(self, amount):
        new_balance = self._balance + amount
        deposit_time = Account._current_time()
        db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))  # noqa
        db.execute("INSERT INTO history VALUES(?, ?, ?)", (deposit_time, self.name, amount))  # noqa
        db.commit()
        self._balance = new_balance

    def deposit(self, amount: int) -> float:
        if amount > 0.0:
            # new_balance = self._balance + amount
            # deposit_time = Account._current_time()
            # db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))  # noqa
            # db.execute("INSERT INTO history VALUES(?, ?, ?)", (deposit_time, self.name, amount))  # noqa
            # db.commit()
            # self._balance = new_balance
            self._save_update(amount)
            print("{:.2f} deposited".format(amount / 100))
        return self._balance / 100

    def withdraw(self, amount: int) -> float:
        if 0 < amount <= self._balance:
            # new_balance = self._balance - amount
            # withdrawal_time = Account._current_time()
            # db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))  # noqa
            # db.execute("INSERT INTO history VALUES(?, ?, ?)", (withdrawal_time, self.name, -amount))  # noqa
            # db.commit()
            # self.balance = new_balance
            # self._save_update(-amount)
            self._save_update(-amount)
            print("{:.2f} withdrawn".format(amount / 100))
            return amount / 100
        else:
            print("The amount must be greater than zero and no more than your account balance")  # noqa: E501
            return 0.0

    def show_balance(self):
        print("Balance on account {} is {:.2f}".format(self.name, self._balance / 100))  # noqa


if __name__ == '__main__':
    john = Account("John")
    john.deposit(5000)
    john.deposit(10)
    john.deposit(10)
    john.withdraw(30)
    john.withdraw(0)
    john.show_balance()

    terry = Account("TerryJ")
    graham = Account("Graham", 9000)
    eric = Account("Eric", 7000)
    michael = Account("Michael")
    terryG = Account("TerryG")

    db.close()
