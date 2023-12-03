def anagram(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    # checking for same number of letters in both the strings

    if len(s1) != len(s2):
        return False

    # Counting frequency of each letter
    count = {}

    # for every letter in s1, if it is present in count
    # then increase its frequency
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    # doing reverse of above situation for s2
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False

    return True


x = anagram('Clint Eastwood', 'Old West Action')
print(x)

y = anagram('Dog', 'God')
print(y)

z = anagram('Public Relations', 'Crap Built on Lies')
print(z)

