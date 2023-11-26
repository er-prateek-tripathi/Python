class Phone:

    def __init__(self, price, brand, camera):
        print("Inside Phone Constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("buying a phone")


class SmartPhone(Phone):

    def buy(self):
        print("Buying a Smart Phone")
        super().buy()


s = SmartPhone(20000, "Apple", 13)

s.buy()

'''

With the use of super keyword, 
methods from parent class can be invoked.
it doesnt work outside class


Here the flow will be

line 26 will call buy() at line 21
line 21 will call class Phone, which will invoke the constructor
and later buy() in Smartphone will be executed completely
after that buy() in Phone will be invoked due to super keyword
'''