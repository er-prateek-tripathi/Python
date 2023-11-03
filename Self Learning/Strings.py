# indexing = gives access to a sequence's
# element eg: str, list, tuple

str = "pragya loves Prateek!!"

if str[0].islower():
    str = str.capitalize()

print(str)

first = str[:6].upper()
print(first)
bond = str[7:13].upper()
print(bond)
last = str[-9:-2].upper()
print(last)

last_char = str[-1]
print(last_char)

# str.format() = formatting a string
# according to user needs
# {} = work as a format feild/placeholder
#

job = "Data Analyst"
name = "Prateek"

print("type 1: Mr.{} is working as a {} in LV.".format(name, job))

print("type 2: Mr.{} is working as a {} in LV.".format(job, name))

# using positional arguments
print("type 3: Mr.{1} is working as a {0} in LV.".format(job, name))

# keyword argument, you need to put keys in the format braces
# print("Mr.{name} is working as a {job} in LV."
#       " This code is using key word arguments.".format(name="Prateek", job="developer"))

text = "Mr.{} is working as a {} in LV."
print("type 4:", text.format(name, job))

# adding padding to a string
print("type 5: Hello, my name is {:10}, nice to meet you.".format(name))
print("type 5: Hello, my name is {:>10}, nice to meet you.".format(name))
print("type 5: Hello, my name is {:^10}, nice to meet you.".format(name))

number = 1000000
print("Initial value: ", number)

# Floating point(3 decimal places)
print("Floating point(3 decimal places): {:.3f}".format(number))

# converting an un-formatted number into a formatted form
print("International number format: {:,}".format(number))

# Converting into binary format
print("Binary form: {:b}".format(number))

# converting into octal format
print("Octal form: {:o}".format(number))

# converting into hexadecimal format
print("Hexa-decimal form: {:X}".format(number))

# converting into exponential format
print("Exponential form: {:E}".format(number))
