class BankAccount:
    # don't forget to add some default values for these parameters!
    all_accounts = []
    def __init__(self, int_rate=None, balance=None):
        if int_rate == None:
            self.int_rate = .07
        else:
            self.int_rate = int_rate
        if balance == None:
            self.balance = 0
        else:
            self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance, amount):
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee.")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.int_rate*self.balance)
        else:
            print("Account Balance must be positive to yield interest.")
        return self

    @staticmethod
    def can_withdraw(balance, amount):
        if (balance - amount) < 0:
            return False
        else:
            return True
    
    @classmethod
    def display_all_balances(cls):
        counter = 1
        for account in cls.all_accounts:
            print(f"Account #{counter} Interest rate: {account.int_rate} Balance: {account.balance}")
            counter += 1


account1 = BankAccount(.05, 200)
account2 = BankAccount(.09, 7000)

# 1st account - 3 deposits, 1 withdrawal, yield interest and display info
account1.deposit(200).deposit(500).deposit(700).withdraw(1000).yield_interest().display_account_info()
# 2nd account - 2 deposits, 4 withdrawals, yield interest and display info

account2.deposit(8000).deposit(9000).withdraw(5000).withdraw(500).withdraw(3000).withdraw(2000).yield_interest().display_account_info()

BankAccount.display_all_balances()