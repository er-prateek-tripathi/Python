class Phone:
    def __init__(self, price, brand, camera):
        print("Inside Phone Constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("buying a phone")


class SmartPhone(Phone):
    pass


SmartPhone(10000, "Apple", "13px").buy()
