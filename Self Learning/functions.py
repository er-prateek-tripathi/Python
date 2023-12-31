# function = a block of code which is executed
# only when it is called
# Keyword Arguments: arguments preceded by an identifier



def love(she, me, age):
    print("know that: " + she + " loves " + me)
    print("her age is " + str(age) + " and my age is " + str(age))
    print("Hope this comes to be true!!\n\n")
    return she + me


# Keyword Argument: writing the name of the arguments
# while passing the value. Here order doesn't matter
love(me="Prateek", she="Pragya", age=23)

# Positional Arguments: Providing values to the arguments
# in an ordered manner. Here order of parameters does matter.
love("Pragya", "Prateek", 23)
love("Pragya", "Prateek", 23)
love("Pragya", "Prateek", 23)
love("Pragya", "Prateek", 23)
print(love("Pragya", "Prateek", 23))

print("\n n1 = 8, n2 = 4")


num1 = 8
num2 = 4


def power(n1, n2):
    print("power function")
    return n1 ** n2


print(power(num1, num2))
# x = power(num1, num2)
# print(x)
# both are same


def multiply(n1, n2):
    print("multiply function")
    return n1 * n2


print(multiply(num1, num2))


def add(n1, n2):
    print("addition function")
    return n1 + n2


print(add(num1, num2))


def sub(n1, n2):
    print("subtraction function")
    return n1 - n2


print(sub(num1, num2))


def div(n1, n2):
    print("division function")
    return n1 / n2


print(div(num1, num2))


def rem(n1, n2):
    print("reminder function")
    return n1 % n2


print(rem(num1, num2))


def quotient(n1, n2):
    print("quotient function")
    return n1 // n2


print(quotient(num1, num2))


# nested function calls: function calls inside other
# function calls.
# Inner most function is executed/resolved first.
# The return value of each nested function is used as
# argument for the outer function.
num = 65.589
num = float(num)
num = abs(num)
num = round(num)
print(num)

# nested way
print(round(abs(float(65.589))))


# scope of a variable: The region that a variable is recognised
# If not declared global or local scope, a variable's scope is
# within its function.

name = "Prateek Tripathi"
print(name)
# global scoped: available inside and outside function


def display_name():
    name = "Pragya"
    # local scope: available inside the function only
    print(name)


display_name()

