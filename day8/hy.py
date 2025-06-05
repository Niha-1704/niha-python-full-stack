from abc import ABC, abstractmethod

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
        print("Amount deposited:", amount)

    def withDraw(self, amount):
        if self.__balance < amount:
            print("Withdraw not possible. Not enough balance.")
        else:
            self.__balance -= amount
            print("Amount withdrawn:", amount)

class CurrentAccount(Account):
    def __init__(self, limit):
        self.__balance = 0
        self.withDraw_limit = limit

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount
        print("Amount deposited:", amount)

    def withDraw(self, amount):
        if self.__balance + self.withDraw_limit < amount:
            print("Not enough balance including overdraft.")
        else:
            self.__balance -= amount
            print("Amount withdrawn:", amount)

class Bank:
    def __init__(self, name, number, account_type="Saving"):
        self.owner = name
        self.account_number = number
        if account_type.lower() == "saving":
            self.account = SavingAccount()
        else:
            self.account = CurrentAccount(5000)

class Manager:
    def get_customer_info(self, bankAccount: Bank):
        print(f"\nName: {bankAccount.owner}")
        print(f"Account Number: {bankAccount.account_number}")
        print("Account Type: ", end="")
        #print("Savings Account" if isinstance(bankAccount.account, SavingAccount) else "Current Account")
        if(type(bankAccount.account) == SavingAccount):
            print("Savings Account")
        else:
            print("Current Account")
        print(f"Balance: {bankAccount.account.get_balance()}\n")

    def __str__(self):
        return "Manager Object bro"
 

m = Manager()
accounts = {}

while True:
    print("\nWelcome to Banking System")
    print("1. Create Account")
    print("2. View Account")
    print("3. Deposit Amount")
    print("4. Withdraw Amount")
    print("5. Balance")
    print("6. Exit")

    try:
        n = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if n == 1:
        name = input("Enter account holder name: ")
        number = int(input("Enter account number: "))
        account_type = input("Enter type of account (Saving/Current): ")
        b = Bank(name, number, account_type)
        accounts[number] = b
        print("Account created.")

    elif n == 2:
        number = int(input("Enter account number to view: "))
        if number in accounts:
            m.get_customer_info(accounts[number])
        else:
            print("Account not found.")

    elif n == 3:
        number = int(input("Enter account number: "))
        if number in accounts:
            amount = float(input("Enter amount to deposit: "))
            accounts[number].account.deposit(amount)
        else:
            print("Account not found.")

    elif n == 4:
        number = int(input("Enter account number: "))
        if number in accounts:
            amount = float(input("Enter amount to withdraw: "))
            accounts[number].account.withDraw(amount)
        else:
            print("Account not found.")

    elif n == 5:
        number = int(input("Enter account number: "))
        if number in accounts:
            balance = accounts[number].account.get_balance()
            print(f"Available Balance: {balance}")
        else:
            print("Account not found.")

    elif n == 6:
        print("Exiting Banking System.")
        break

    else:
        print("Invalid choice. Please try again.")
