import random


class BankAccount(object):
    def __init__(self, username, accountType, balance=0):
        self.name = username
        self.accountType = accountType
        self.balance = balance
        self.accountNumber = random.randint(10000, 99999)

        self.filename = str(self.accountNumber) + "_" + self.accountType + "_" + self.name + ".txt"

        with open(self.filename, "w") as file:
            file.write("Bank Account Statement\n")
            file.write("----------------------\n")
            file.write("Username: " + self.name + "\n")
            file.write("Account Type: " + self.accountType + "\n")
            file.write("Account Number: " + str(self.accountNumber) + "\n")
            file.write("Starting Balance: $" + str(self.balance) + "\n\n")

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return

        self.balance += amount

        with open(self.filename, "a") as file:
            file.write("Deposit: $" + str(amount) + "\n")
            file.write("New Balance: $" + str(self.balance) + "\n\n")

        print("Deposit successful.")
        print("Current balance:", self.balance)

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        if amount > self.balance:
            print("You cannot withdraw more than your current balance.")
            return

        self.balance -= amount

        with open(self.filename, "a") as file:
            file.write("Withdrawal: $" + str(amount) + "\n")
            file.write("New Balance: $" + str(self.balance) + "\n\n")

        print("Withdrawal successful.")
        print("Current balance:", self.balance)

    def get_balance(self):
        return self.balance

    def get_user_id(self):
        return self.accountNumber

    def get_username(self):
        return self.name

    def get_account_type(self):
        return self.accountType

    def get_transaction_history(self):
        with open(self.filename, "r") as file:
            history = file.read()
        return history


# Testing the code by creating multiple objects and applying transactions

account1 = BankAccount("Koorosh", "checking", 100)
account1.deposit(50)
account1.withdraw(30)

print("Account 1 Balance:", account1.get_balance())
print("Account 1 ID:", account1.get_user_id())
print("Account 1 Username:", account1.get_username())
print("Account 1 Type:", account1.get_account_type())
print(account1.get_transaction_history())


account2 = BankAccount("Sara", "saving", 200)
account2.deposit(100)
account2.withdraw(50)

print("Account 2 Balance:", account2.get_balance())
print("Account 2 ID:", account2.get_user_id())
print("Account 2 Username:", account2.get_username())
print("Account 2 Type:", account2.get_account_type())
print(account2.get_transaction_history())
