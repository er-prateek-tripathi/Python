class Parent:

    def __init__(self, num):
        self.__num = num  # making a variable private

    def get_num(self):
        return self.__num


class Child(Parent):

    def __init__(self, val, num):
        self.__val = val

    def get_val(self):
        return self.__val


son = Child(100, 10)
# print("Parent: Num: ", son.get_num())  # init of parent didn't trigger, that's why error came
print("Child: Val: ", son.get_val())

# if child class already has a init constructor, so parents init constructor won't be called.
