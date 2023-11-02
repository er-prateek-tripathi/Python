# while loop = a loop whose statement will be
# executed as long as the condition mentioned
# in the loop stands true.

# while 1 == 1:
#     print("stuck!")
# Infinite loop

name = ""

while len(name) == 0:
    name = input("Enter your name: ")

print("Hello " + name)
