# *args = a parameter that will pack all arguments into
# a tuple. It is useful so that a function can accept a
# varying amount of arguments

def add(*nums):
    sum = 0
    # nums[0] = 0
    # this line is trying to mutate a tuple, so error is thrown
    nums = list(nums)
    # this is done because *args is initially tuple
    for i in nums:
        sum += i
    return sum


print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# **kwargs = a parameter that will pack all the arguments
# into a dictionary.
# Helps a function to accept varying amount of key-value arguments


def func(**kwargs):
    print("Hello " + kwargs['first'] + " " + kwargs['last'])
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")


func(title="Mr.", first="Prateek", middle="Loves", last="Pragya")
