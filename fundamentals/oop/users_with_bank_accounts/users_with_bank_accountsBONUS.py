class BankAccount:
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
            print(
                f"Account #{counter} Interest rate: {account.int_rate} Balance: {account.balance}")
            counter += 1


# class SavingsAccount(BankAccount):
#     def __init__(self,balance=0, int_rate = 1.15):
#         super().__init__(balance)

#     def withdraw(self, amount, is_early):
#         if is_early:
#             amount = amount * 1.10
#         super().withdraw(amount)
#         return self


class User:
    def __init__(self, name, email_address):
        self.email = email_address
        self.name = name
        self.accounts = {"checking": BankAccount(int_rate=0.02, balance=0)}

    def make_deposit(self, amount, type):
        self.accounts[f'{type}'].deposit(amount)
        return self

    def make_withdrawal(self, amount, type):
        self.accounts[f'{type}'].withdraw(amount)
        return self

    def display_user_balance(self):
        for account in self.accounts:
            print(f"User: {self.name}, {account.title()} Account Balance: ${self.accounts[f'{account}'].balance}")
            # print(account)
        return self

    def transfer_money(self, other_user, amount):
        self.account.balance -= amount
        other_user.account.balance += amount

    def add_new_account(self, type, int_rate, balance):
        self.accounts[f'{type}'] = BankAccount(int_rate, balance)


nick = User("Nick Smart", "nsmart@python.com")
seth = User("Seth Sethberg", "ssethberg@python.com")
dylan = User("Dylan Dylanopolous", "ddylanopolous@python.com")

nick.make_deposit(100, "checking").make_deposit(200, "checking").make_deposit(
    275, "checking").make_withdrawal(250, "checking")

nick.add_new_account("savings", 1.10, 20000)

nick.display_user_balance()


# Have second user make 2 deposits, 2 withdrawals, display balance
# seth.make_deposit(500).make_deposit(300).make_withdrawal(
#     175).make_withdrawal(50).display_user_balance()


# Have third user make 1 deposit and 3 withdrawals, then display balance
# dylan.make_deposit(1000).make_withdrawal(700).make_withdrawal(
#     275).make_withdrawal(150).display_user_balance()
