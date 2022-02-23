# For this assignment, we'll add some functionality to the User class:

# make_withdrawal(self, amount) - have this method decrease the user's
# balance by the amount specified
# display_user_balance(self) - have this method print the user's name
# and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150

# BONUS: transfer_money(self, other_user, amount) -
# have this method decrease the user's balance by the
# amount and add that amount to other other_user's balance

class User:
    def __init__(self, name, email_address):
        self.name = name
        self.account_balance = 0
        self.email = email_address

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount

nick = User("Nick Smart", "nsmart@python.com")
seth = User("Seth Sethberg", "ssethberg@python.com")
dylan = User("Dylan Dylanopolous", "ddylanopolous@python.com")


# Have first user make 3 deposits, 1 withdrawal and display balance
nick.make_deposit(100)
nick.make_deposit(200)
nick.make_deposit(275)
nick.make_withdrawal(250)
nick.display_user_balance()

# Have second user make 2 deposits, 2 withdrawals, display balance
seth.make_deposit(500)
seth.make_deposit(300)
seth.make_withdrawal(175)
seth.make_withdrawal(50)
seth.display_user_balance()

# Have third user make 1 deposit and 3 withdrawals, then display balance
dylan.make_deposit(1000)
dylan.make_withdrawal(700)
dylan.make_withdrawal(275)
dylan.make_withdrawal(150)
dylan.display_user_balance()

# Add transfer_money method; have first user transfer money to third user and
# print both user's balances
nick.transfer_money(dylan, 125)
print("Nick transfers $125 to Dylan to get him out of the red!")
nick.display_user_balance()
dylan.display_user_balance()