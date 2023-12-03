"""
Take a string and return character that never repeats
if multiple uniques, return only the first unique
character.
"""


def non_Repeating(s):
    s = s.replace(' ', '').lower()

    char_count = {}

    for c in s:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1

    uniques = []
    y = sorted(char_count.items(), key=lambda x: x[1])

    for items in y:
        if items[1] == y[0][1]:
            uniques.append(items)

    return uniques


print(non_Repeating('I Apple Ape Peels'))
