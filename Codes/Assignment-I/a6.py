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
