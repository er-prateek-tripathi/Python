"""
Given an array, what is the most frequent element
"""


def frequent(arr):
    count = {}

    max_count = 0
    max_item = None

    for i in arr:
        if i not in count:
            count[i] = 1

        else:
            count[i] += 1

        if count[i] > max_count:
            max_count = count[i]
            max_item = i

    return max_item


ar = [1, 2, 3, 2, 5, 2, 7, 8, 2, 9]
print("Most Frequent Element: ", frequent(ar))
