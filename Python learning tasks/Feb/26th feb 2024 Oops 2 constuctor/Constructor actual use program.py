class Vwologinpage:
    email = None
    password = None

    def __init__(self, o_email, o_password):
        self.email = o_email
        self.password = o_password

    def loginconfirm(self):
        if self.password == "Faraz@123":
            print("Welcome to Vwo Platform")
        else:
            print("Your password is wrong")


faraz = Vwologinpage("faraz@gmail.com", "Faraz@123")
faraz.loginconfirm()
print("=============================================")
aafi = Vwologinpage("aafi@gmail.com", "Faraz@1234")
aafi.loginconfirm()

print(id(faraz))
print(id(aafi))