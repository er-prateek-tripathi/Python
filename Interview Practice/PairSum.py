"""

Array Pair sum

Give an integer array,
output all the unique pairs, which sum total to K

Input: arr = [1,2,4,5,6,3,2,7,4], k = 8
Output: (4, 4)
        (1, 7)
        (2, 6)
        (3, 5)

"""


def pair_sum(arr, k):

    if len(arr) < 2:
        return print('Too Small!!')

    seen = set()
    output = set()

    for num in arr:
        target = k - num

        if target not in seen:
            seen.add(num)

        else:
            output.add((min(num, target), max(num, target)))

    print('\n'.join(map(str, list(output))))


array = [1, 2, 4, 5, 6, 3, 2, 7, 4]
n = 8
pair_sum(array, n)
