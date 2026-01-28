class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount")
            return
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
            return
        self.balance -= amount
        print(f"Withdrawn {amount}. Remaining balance is {self.balance}")

    def __str__(self):
        return f"Account Holder: {self.account_holder}, Balance: {self.balance}"

class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if self.balance - amount < 500:
            print("Minimum balance of 500 required")
            return
        super().withdraw(amount)

class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        overdraft_limit = 1000
        if amount > self.balance + overdraft_limit:
            print("Overdraft limit exceeded")
            return
        self.balance -= amount
        print(f"Withdrawn {amount}. Balance is now {self.balance}")

if __name__ == "__main__":
    acc1 = SavingsAccount("Ali", 2000)
    acc2 = CurrentAccount("Ahmed", 1000)

    acc1.deposit(500)
    acc1.withdraw(1800)

    acc2.withdraw(1500)
    print(acc1)
    print(acc2)
