class Phone():
    def __init__(self, price, brand, camera):
        print("Inside Phone Constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("buying a phone")


class FeaturePhone(Phone):
    pass


class SmartPhone(Phone):
    pass


s = SmartPhone(20000, 'Apple', 12)

s.buy()
