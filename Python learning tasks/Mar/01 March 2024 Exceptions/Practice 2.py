class MyCustomException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)
balance = 100
withdraw_amount = int(input("How much amount you wants to withdraw?:-"))
if withdraw_amount > balance:
    raise MyCustomException("Your Balance is Low")
else:
    print("Total balance after withdraw is:-", balance-withdraw_amount)

