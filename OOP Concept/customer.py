class Customer:

    def __init__(self, name):
        self.name = name


def greet(customer):

    print("Hello ", customer.name)


cust = Customer("Prateek")  # Object Creation
greet(cust)  # passing an object in a function

