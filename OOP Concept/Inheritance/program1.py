class Parent:

    def __init__(self, num):
        self.__num = num  # making a variable private

    def get_num(self):
        return self.__num


class Child(Parent):

    def show(self):
        print("Child Class")


son = Child(100)
print(son.get_num())
son.show()
