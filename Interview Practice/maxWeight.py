"""

Given a list of items with values and weights,
as well as max weight. find the maximum value you
can generate from items where the sum of the
weights is less than the max.

Input:
weights = [10, 20, 30]
values = [60, 100, 120]
max_weight = 50

Output: 220

"""


def knapsack(weights, values, max_weight):
    n = len(weights)
    dp = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, max_weight + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][max_weight]


weights = [10, 20, 30]
values = [60, 100, 120]
max_weight = 50

print(knapsack(weights, values, max_weight))
