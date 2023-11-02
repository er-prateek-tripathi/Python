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
