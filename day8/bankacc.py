from abc import ABC, abstractmethod
import os

class Account(ABC):

    @abstractmethod
    def get_balance(self):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withDraw(self, amount):
        pass

class SavingAccount(Account):

    def __init__(self):
        self.__balance = 0

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount
        print("Amount deposited: ", amount)

    def withDraw(self, amount):
        if self.__balance < amount:
            print("Not Enough Balance")
            return
            
        self.__balance -= amount
        print("Amount withdrawn: ", amount)

class CurrentAccount(Account):

    def __init__(self, limit):
        self.__balance = 0
        self.withDraw_limit = limit

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount
        print("Amount deposited: ", amount)

    def withDraw(self, amount):
        if self.__balance + self.withDraw_limit < amount:
            print("Not Enough Balance")
            return

        self.__balance -= amount
        print("Amount withdrawn: ", amount)

class Bank:

    def __init__(self, name, number, account_type="Saving"):
        self.owner = name
        self.account_number = number

        if account_type == "Saving":
            self.account = SavingAccount()
        elif account_type == "Current":
            self.account = CurrentAccount(5000)

    def save_to_file(self):
        x=open("accounts.txt", "a")
        x.write(f"{self.owner},{self.account_number},{self.account.get_balance()},{type(self.account)}\n")

    @staticmethod
    def load_accounts():
        accounts = {}
        if os.path.exists("accounts.txt"):
            with open("accounts.txt", "r") as file:
                for line in file:
                    name, number, balance, account_type = line.strip().split(',')
                    number = int(number)
                    balance = float(balance)
                    bank = Bank(name, number, account_type)
                    bank.account.deposit(balance)  # Set the initial balance
                    accounts[number] = bank
        return accounts

class Manager:

    def get_customer_info(self, bankAccount: Bank):
        print(f"Name: {bankAccount.owner}")
        print(f"Account Number: {bankAccount.account_number}")
        print("Account Type: ", end="")
        if isinstance(bankAccount.account, SavingAccount):
            print("Savings Account")
        else:
            print("Current Account")
        print(f"Balance: {bankAccount.account.get_balance()}")

    def __str__(self):
        return "Manager Object"

# Load existing accounts from file
accounts = Bank.load_accounts()
manager = Manager()

while True:
    print("\nBank Application")
    print("1. Create Account")
    print("2. Account Details")
    print("3. Deposit Amount")
    print("4. Withdraw Amount")
    print("5. Exit from bank")
    n = int(input("Enter the choice: "))
    
    if n == 1:
        name = input("Enter account holder name: ")
        number = int(input("Enter account number: "))
        acc_type = input("Enter account type (Saving/Current): ")
        accounts[number] = Bank(name, number, acc_type)
        accounts[number].save_to_file()  # Save account to file
        print("Account is created")
        
    elif n == 2:
        acc_number = int(input("Enter account number to view details: "))
        if acc_number in accounts:
            manager.get_customer_info(accounts[acc_number])
        else:
            print("Account not found")
            
    elif n == 3:
        acc_number = int(input("Enter account number to deposit: "))
        if acc_number in accounts:
            amount = float(input("Enter amount to deposit: "))
            accounts[acc_number].account.deposit(amount)
        else:
            print("Account not found")

    elif n == 4:
        acc_number = int(input("Enter account number to withdraw: "))
        if acc_number in accounts:
            amount = float(input("Enter amount to withdraw: "))
            accounts[acc_number].account.withDraw(amount)
        else:
            print("Account not found")
            
    elif n == 5:
        print("Exiting the program")
        break
        
    else:
        print("Invalid choice")
