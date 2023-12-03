"""

Finding Common elements in Two Sorted Arrays

return the common elements as an array.

Ex:

Input: arr1 = [1, 3, 4, 7, 6, 9]
       arr2 = [3, 2, 4, 5, 6, 1]

Output: [1, 3, 4, 6]

"""


# Time Complexity : O(n^2)
def common_elements1(lst1, lst2):
    common = []

    for i in range(len(lst1)):
        for j in range(len(lst2)):
            if lst1[i] == lst2[j]:
                if lst1[i] not in common:
                    common.append(lst1[i])

    return common


arr1 = [1, 3, 4, 7, 6, 9]
arr2 = [3, 2, 5, 4, 6, 1]

print(common_elements1(arr1, arr2))



# Time Complexity : O(n + m)
def common_elements(lst1, lst2):
    p1 = 0
    p2 = 0

    result = []

    while p1 < len(lst1) and p2 < len(lst2):
        if lst1[p1] == lst2[p2]:
            result.append(lst1[p1])
            p1 += 1
            p2 += 1

        elif lst1[p1] < lst2[p2]:
            p1 += 1

        else:
            p2 += 1

    return result


arr1 = [1, 3, 4, 6, 7, 9]
arr2 = [1, 2, 3, 4, 5, 6]

print(common_elements(arr1, arr2))
