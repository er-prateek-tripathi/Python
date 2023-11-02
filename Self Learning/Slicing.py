'''
String Slicing:
creating  substring by extracting elements from another
string.
[start:stop:step]

'''

name = "Prateek and Pragya"

first_name = name[:7]
print(first_name)

second_name = name[12:]
print(second_name)

funky_name = name[::2]
print(funky_name)

reversed_name = name[::-1]
print(reversed_name)

website1 = "https://google.com"
website2 = "https://wikipedia.com"
slice = slice(8,-4)
print(website1[slice])
print(website2[slice])
