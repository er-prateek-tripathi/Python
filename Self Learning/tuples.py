# tuple = collection which is ordered and uchageable.
# it is used to grop together related data.

student = ("Prateek", 23, "Pragya")

# number of times an element is present in the tuple
print(student.count("Prateek"))

# finding index of an element
print(student.index("Pragya"))

# Printing elements of a list
for x in student:
    print(x)

# checking availability of element
if "Pragya" in student:
    print("Pragya will marry Prateek.")