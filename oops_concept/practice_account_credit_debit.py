 # create account class with 2 attributes - Balance and Account No.
 # Create methods for debit, credit, & printing the balance

class Account:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no

    def debit(self, amount):
        self.balance = self.balance - amount
        print("Rs.", amount, "was debited from")
        print("Your current balance is:", self.get_balance())

    def credit(self, amount):
        self.balance = self.balance + amount
        print("Rs.", amount, "was credited from")
        print("Your current balance is:", self.get_balance())

    def get_balance(self):
        return self.balance



c1 = Account(10000, 1234)
c1.debit(1000)
c1.credit(2000)
c1.get_balance()
print(c1.get_balance())
