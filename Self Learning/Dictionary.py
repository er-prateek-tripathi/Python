# dictionary = A changeable, unordered collection
# of unique key:value pairs.
# Fast because they use hashing, allows us to
# access a value quickly

capitals = {'USA': 'Washington DC',
            'India': 'New Delhi',
            'China': 'Beijing',
            'Russia': 'Moscow'}

# adding new pair
capitals.update({'Germany': 'Berlin'})
print(capitals)

# updating available value
capitals.update({'USA': 'Las Vegas'})
print(capitals)

# popping a pair
capitals.pop('China')
print(capitals)

# deleting the pairs in the dictionary
# capitals.clear()
# print(capitals)

# Accessing value using keys
print(capitals['Germany'])
print(capitals.get('Germany'))

for key,value in capitals.items():
    print(key,value)