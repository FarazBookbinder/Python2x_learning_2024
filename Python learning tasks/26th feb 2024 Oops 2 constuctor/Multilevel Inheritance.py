class Grand_father:
    gf_properties = "5 BHK Flat"
    net_worth = "2 billion $"

    def gf_main_properties(self):
        print("Main property is in mumbai and it's", self.gf_properties)

    def gf_net_worth(self):
        print("Grand father net worth is", self.net_worth)


class Father(Grand_father):
    father_properties = "3 BHK Bungalow"
    father_net_worth = "2 billion $"

    def father_main_properties(self):
        print("Main property is in dubai and it's", self.father_properties)

    def father_net_worth(self):
        print("Father net worth is", self.father_net_worth)

class Son(Father):
    pass

obj1 = Son()
obj1.gf_main_properties()
obj1.gf_net_worth()
print(obj1.gf_properties)
print(obj1.gf_net_worth)
obj1.father_main_properties()
obj1.father_main_properties()
print(obj1.father_properties)
print(obj1.father_net_worth)