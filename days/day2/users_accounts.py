class User():

    def __init__(self):
        self.account = BankAccount()

    def make_deposit(self, amount):
        # self.account.balance += amount
        self.account.deposit_into_account(amount)


class BankAccount():

    def __init__(self):
        self.balance = 0
    
    def deposit_into_account(self, amount):
        self.balance += amount
