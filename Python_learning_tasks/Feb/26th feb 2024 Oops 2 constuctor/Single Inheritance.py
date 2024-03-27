class Father:
    gold = "5kg"
    platinum = "10kg"
    __Private_house = "Beach House"

    def car_brand(self):
        print("Lamborghini")

    def properties(self):
        print("200 km plot")

    def private_house_access(self, only_my_son):
        print("My only son have access to use my", self.__Private_house)


class Son(Father):
    house = "4 BHK flat in mumbai"
    car = "BMW"

    def house_mumbai(self):
        print("In Mumbai", self.house)

    def car_brand_is(self):
        print("Brand is", self.car)


faruk = Father()
faruk.car_brand()
faruk.properties()
faruk.private_house_access(True)

print("-------------------------------------")

faraz = Son()
faraz.properties()
faraz.car_brand()
faraz.house_mumbai()
faraz.car_brand_is()
faraz.private_house_access(True)
print(faraz.car)
print(faraz.house)
print(faraz.gold)
print(faraz.platinum)
