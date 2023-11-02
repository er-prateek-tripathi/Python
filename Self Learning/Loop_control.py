# Loop control statements = these statements
# change the loop execution flow from default
# way to their customized way.

# break = used to terminate the loop entirely
# continue = skips to the next iteration of the loop
# pass = does nothing, acts as a placeholder

while True:
    name = input("Enter your name: ")
    if name != "":
        break

phone_number = "123-456-7890"

for i in phone_number:
    if i == "-":
        continue
    print(i, end=" ")

for i in range(1, 10):
    if i == 7:
        pass
    else:
        print(i)
