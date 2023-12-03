"""

Given 2 distinct arrays,
is array1 a rotation of another: return True/False

rotated array: Same size and elements, start index is different

Time complexity: O(n)

Go through:

select an indexed position in list1 and get its value
Find same value in list2.
check index for index
if any variation, return False
Getting last item without False: True

"""


def isRotated(list1, list2):

    if len(list1) != len(list2):
        return False

    key = list1[0]

    key_index = 0

    for i in range(len(list2)):

        if list2[i] == key:
            key_index = i

            break

    if key_index == 0:
        return False

    for x in range(len(list1)):
        l2_index = (key_index + x) % len(list1)

        if list1[x] != list2[l2_index]:
            return False

    return True


arr1 = [1, 2, 3, 4, 5, 6, 7, 8]
arr2 = [4, 5, 6, 7, 8, 1, 2, 3]
print(isRotated(arr1, arr2))
