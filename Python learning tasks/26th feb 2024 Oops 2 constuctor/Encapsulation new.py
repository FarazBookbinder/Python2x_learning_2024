class Password:
    def __init__(self, password):
        self.__password = password
        self.publ_var = 10
    def get_password(self, is_auth):
        if is_auth:
            print(self.__password)
        else:
            print("Invalid Password")
    def set_password(self, password):
        if len(password) >= 10:
            self.__password = password
        else:
            print("Entered Password is weak..")


obj = Password("Aafraz@123")
obj.get_password(True)
obj.set_password("Faraz")




