class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self.balance

class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def transfer_funds(self, from_account_number, to_account_number, amount):
        from_account = self.find_account(from_account_number)
        to_account = self.find_account(to_account_number)

        if from_account and to_account:
            if from_account.get_balance() >= amount:
                from_account.withdraw(amount)
                to_account.deposit(amount)
                print("Funds transferred successfully.")
            else:
                print("Insufficient funds in the source account.")
        else:
            print("One or both accounts not found.")

    def display_all_accounts(self):
        print("\nAll Accounts:")
        for account in self.accounts:
            print(f"Account Number: {account.account_number}")
            print(f"Account Holder: {account.account_holder}")
            print(f"Balance: ${account.get_balance()}")
            print("-----------------------")

# Example usage with user input:
bank = Bank()

# Creating accounts with initial balance
num_accounts = int(input("Enter the number of accounts to create: "))
for i in range(num_accounts):
    account_number = input(f"Enter account number for Account {i + 1}: ")
    account_holder = input(f"Enter account holder name for Account {i + 1}: ")
    initial_balance = float(input(f"Enter initial balance for Account {i + 1}: "))
    new_account = BankAccount(account_number, account_holder, initial_balance)
    bank.add_account(new_account)

bank.display_all_accounts()

# Displaying initial account balances
print("\nInitial Account Balances:")
for account in bank.accounts:
    print(f"Account {account.account_number} - Balance: ${account.get_balance()}")

# Transferring funds
from_account_num = input("\nEnter source account number for fund transfer: ")
to_account_num = input("Enter destination account number for fund transfer: ")
transfer_amount = float(input("Enter the amount to transfer: "))

bank.transfer_funds(from_account_num, to_account_num, transfer_amount)

# Displaying updated account balances
print("\nUpdated Account Balances:")
for account in bank.accounts:
    print(f"Account {account.account_number} - Balance: ${account.get_balance()}")


# EXPLANATION OF THE ABOVE CODE - 

# This code defines two classes, `BankAccount` and `Bank`, which simulate a basic banking system. It allows users to create bank accounts, deposit and withdraw funds, and transfer funds between accounts.

# BankAccount class:

# - __init__(self, account_number, account_holder, initial_balance=0): Initializes a bank account with an account number, account holder name, and an optional initial balance (default is 0).
  
# - deposit(self, amount): Adds the specified amount to the account balance.

# - withdraw(self, amount): Subtracts the specified amount from the account balance, but only if there are sufficient funds. If not, it prints "Insufficient funds!"

# - get_balance(self): Returns the current account balance.

# Bank class:

# - __init__(self): Initializes a bank with an empty list of accounts.

# - add_account(self, account): Adds a BankAccount instance to the list of accounts.

# - find_account(self, account_number): Finds and returns a BankAccount instance based on the provided account number. Returns None if the account is not found.

# - transfer_funds(self, from_account_number, to_account_number, amount): Transfers funds from one account to another. It first finds the source and destination accounts using the account numbers. If both accounts exist, it checks if the source account has sufficient funds. If so, it transfers the specified amount from the source to the destination account and prints "Funds transferred successfully." Otherwise, it prints "Insufficient funds in the source account" or "One or both accounts not found."

# Example usage:

# 1. The user is prompted to input the number of accounts to create and details for each account, including the account number, account holder name, and initial balance.

# 2. Initial account balances are displayed.

# 3. The user is prompted to enter source and destination account numbers and the amount to transfer.

# 4. The transfer_funds method is called to transfer funds between accounts.

# 5. Updated account balances are displayed after the funds transfer.

