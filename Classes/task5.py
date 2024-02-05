class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please deposit a positive amount.")
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print("Insufficient funds. Withdrawal not allowed.")
        else:
            print("Invalid withdrawal amount. Please withdraw a positive amount.")
account1 = Account(owner="John Doe", balance=1000)
account1.deposit(500)
account1.withdraw(200)
account1.withdraw(800)
account1.deposit(1000)
account1.withdraw(2000)
