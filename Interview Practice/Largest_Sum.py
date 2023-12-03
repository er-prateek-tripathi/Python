"""
Take an array with positive and negative integers and
find the maximum su of tha array

input: arr = [45, 23, -91, 85, -7, -85, 0, -21, -77, 84]
output: 85
"""


def largest(arr):
    if len(arr) == 0:
        return print('Too small!!')

    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)

    return max_sum


array = [45, 23, -91, 85, -7, -85, 0, -21, -77, 84]
print(largest(array))
