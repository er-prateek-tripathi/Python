# list = used to store multiple items in single variable
# it can be updated and changed any time.
food = ["pizza", "chaat", "burger", "paneer-tikka"]

food[0] = "Chowmein"

print(food)

# for loop
for x in food:
    print(x)

# adding element in a list
food.append("ice-cream")
print(food)

# removing desired element from list
food.remove("burger")
print(food)

# popping is same as removing, but it pos from the end of list
food.pop()
print(food)

# inserting an element at desired index
food.insert(0, "Cake")
print(food)

# sorting the list
food.sort()
print(food)

# deleting all the elements from the list, except the list itself
food.clear()
print(food)

# 2D list
# a list of lists

drinks = ["coffee", "soda", "tea", "Soft-Drink"]
dinner = ["pizza", "chowmein", "biryani"]
dessert = ["ice-cream", "faluda", "cup-cake"]

menu = [drinks, dinner, dessert]

print(menu)
print(menu[0][1])  # accessing elements of list within a list

