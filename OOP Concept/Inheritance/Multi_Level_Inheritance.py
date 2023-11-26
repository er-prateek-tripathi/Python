class Product:
    def review(self):
        print("Product Customer Review")


class Phone(Product):
    def __init__(self, price, brand, camera):

        print("Inside Phone Constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("buying a phone")


class SmartPhone(Phone):
    pass


s = SmartPhone(20000,'Apple', 12)
p = Phone(10000, 'One Plus', 10)

s.buy()
s.review()
p.review() 
