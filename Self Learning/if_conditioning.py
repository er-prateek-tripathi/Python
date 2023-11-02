# if statement: a block of code which will be
# executed if the condition mentioned in it is met

age = int(input("How old are you?: "))
if age == 100:
    print("You are a century old!!")
elif age >= 18:
    print("you are an adult!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You are a child!")
