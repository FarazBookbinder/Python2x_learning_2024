class Bank_account_secure:
    def __init__(self):
        self.balance = 0
        self.__private_var = 100
    def deposit(self,amount):
         self.balance += amount
    def __withdraw(self,amount):
        self.balance -= amount
    def __show_balance(self):
        print("Your Balance is:-",self.balance)
    def if_auth(self, flag):
        if flag:
            self.__show_balance()
        else:
            print("You are not allowed")
    def withdraw_with(self, amount):
        self.__withdraw(amount = amount)

    #is able to access __private_var variable throug the function?
    def private_varriale(self):
        print(self.__private_var)

hdfc = Bank_account_secure()
hdfc.deposit(1000)
hdfc.withdraw_with(300)
hdfc.if_auth(False)
hdfc.private_varriale()


