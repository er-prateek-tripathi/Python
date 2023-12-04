"""
Given an array with elements in some range, find the missing numbers.
Input: [1, 3, 5, 6, 7, 9]
Output: [2, 4, 8]
"""


def missing(arr, n):
    missed = []

    for i in range(1, arr[-1] + 1):
        if i not in arr:
            missed.append(i)

    return missed


print(missing([1, 3, 5, 6, 7, 9], 6))

