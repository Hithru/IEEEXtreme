# Challenge Name: Maximum Perimeter
# Difficulty: Easy
from typing import List


def maximum_perimeter(sticks: List[int]):
    sticks.sort()

    for k in range(len(sticks) - 1, 1, -1):
        longest_hand = sticks[k]
        other_hand_sum = sticks[k - 1] + sticks[k - 2]
        if other_hand_sum > longest_hand:
            return [sticks[k - 2], sticks[k - 1], sticks[k]]
    return [-1]


print(maximum_perimeter([1, 3, 2]))
