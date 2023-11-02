# set = an unordered and unindexed collection
# with unique values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

# adding an element in a set
utensils.add("napkin")
print(utensils)

# removing an element from a set
# utensils.remove("fork")
# print(utensils)

# removing all the elements from a set
# utensils.clear()
# print(utensils)

# union will return all the elements from
# set in parentheses
# elements are indexed at random places
dinner_table = utensils.union(dishes)
print("Union", dinner_table)

print("difference", dishes.difference(utensils))
print("Intersection", utensils.intersection(dishes))

for x in dinner_table:
    print(x)