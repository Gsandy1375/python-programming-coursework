# This script simulates a banking system with deposit, withdraw, and transfer functions
# It includes balance checks and prints transaction outcomes demonstrating functionality with three simple accounts

# This defines a blueprint for creating bank account objects with related data and actions
class BankAccount:

    # This creates the account with the holder's name and the balance
    def __init__(self, id, first_name, last_name, balance=0):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance

    # This ads money to the account 
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited $", amount, ". New balance: $", self.balance)
        else:
            print("Invalid deposit amount.")

    # This takes money contigent that there are sufficient funds
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            self.balance -= amount
            print("Withdrew $", amount, ". New balance: $", self.balance)

    # This moves money to another account
    def transfer(self, amount, other_account):
        if amount > self.balance:
            print("Insufficient funds for transfer.")
        elif amount <= 0:
            print("Invalid transfer amount.")
        else:
            self.balance -= amount
            other_account.balance += amount
            print("Transferred $", amount, "to", other_account.first_name, other_account.last_name)

    # This prints account information
    def __str__(self):
        return "Account Holder: " + self.first_name + " " + self.last_name + ", Balance: $" + str(self.balance)

# This creates associated accounts
account1 = BankAccount(1, "John", "Doe", 500)
account2 = BankAccount(2, "Jane", "Doe", 300)
account3 = BankAccount(3, "John", "Smith", 0)

# This tests deposit
account1.deposit(100)
account2.deposit(100)
account3.deposit(100)

# This tests valid withdrawal
account1.withdraw(50)

# This tests withdrawal with insufficient funds
account3.withdraw(500)

# This tests valid transfer
account2.transfer(100, account3)

# This tests transfer with insufficient funds
account3.transfer(1000, account1)

# This prints final account info
print(account1)
print(account2)
print(account3)