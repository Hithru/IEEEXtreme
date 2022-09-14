# Challenge Name: Mark And Toys
# Difficulty: Easy
from typing import List


def maximum_toys(prices: List, k: int):
    prices.sort()
    answer = 0
    for toy in prices:
        k -= toy
        if k < 0:
            break
        answer += 1
    return answer


print(maximum_toys([1, 12, 5, 111, 200, 1000, 10], 50))
