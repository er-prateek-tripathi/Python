class A:

    def m1(self):
        return 20


class B(A):

    def m1(self):
        return 30

    def m2(self):
        return 40


class C(B):

    def m2(self):
        return 20


obj1 = A()
obj2 = B()
obj3 = C()
print(obj1.m1() + obj3.m1() + obj3.m2())
        # 20 + 30 + 20 = 70
# first the method present in the class will be taken in cosideration
# after that if the method is not present in the called class
# look for the method in the inherited class.

# this is called method resolution order
