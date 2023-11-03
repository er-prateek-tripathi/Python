# exception = events detected during
# execution that interrupts the flow of a program

# to handle an exception, use try except block,
# it won't remove it, but it will not show error

try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    result = numerator/denominator
except ZeroDivisionError as e:
    print(e)
    print("Division by zero is not allowed.")
except ValueError as e:
    print(e)
    print("Only numbers are accepted.")
except Exception as e:
    print(e)
    print("Something Went wrong.")
else:
    print(result)
    # executed iff no exception is there
finally:
    # always at the end.
    # whether we catch an exception we will always
    # execute
    # any code that is within
    # the block of code for out finally clause
    print("Finally clause will always be executed.")

