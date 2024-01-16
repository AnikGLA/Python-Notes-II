# Assignment 2:
# Problem Statement:

# Design a BankAccount class with encapsulated attributes for an account holder's name, account number, and balance. Include methods to deposit, withdraw, and display the account information. Ensure that the balance is not accessible directly and provide proper validation for withdrawal to avoid overdraft.

class BankAccount:
    def __init__(self, account_holder, account_number, initial_balance):
        self._account_holder = account_holder
        self._account_number = account_number
        self._balance = initial_balance

    def deposit(self, amount):
        self._balance += amount
        print(f"Deposited ${amount}. New balance: ${self._balance}")

    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient funds. Withdrawal denied.")
        else:
            self._balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self._balance}")

    def display_info(self):
        return f"Account Holder: {self._account_holder}\nAccount Number: {self._account_number}\nBalance: ${self._balance}"

# Create a BankAccount object
account1 = BankAccount("John Doe", "123456789", 1000)

# Demonstrate functionality
print(account1.display_info())
account1.deposit(500)
account1.withdraw(200)
account1.withdraw(800)
print(account1.display_info())
