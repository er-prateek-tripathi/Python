class A:

    def m1(self):
        return 20


class B(A):

    def m1(self):

        val = super().m1() + 30
        return val


class C(B):

    def m1(self):

        val = self.m1() + 20
        return val


obj = C()
print(obj.m1())

'''
Here from line 24, we go to 23
from line 23 we go to CLass C

we look into m1 in C and try to calculate val.
But val is calling itself via obj.

This leads to a infinite recursion cos, the call 
wont go to any other class.
'''
