class Phone():
    def __init__(self, price, brand, camera):
        print("Inside Phone Constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("buying a phone")


class Product:

    def review(self):
        print('customer review')

    def buy(self):
        print("buying a phone from product")


class FeaturePhone(Phone, Product):
    pass


class SmartPhone(Phone, Product):
    pass


s = SmartPhone(20000, 'Apple', 12)
f = FeaturePhone(30000, 'samsung', 50)

s.buy()
s.review()
f.buy()
f.review()
