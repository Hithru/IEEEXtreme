# Challenge Name: Sherlock and Array
# Difficulty: Easy
from typing import List


def sherlock_and_array(arr: List[int]):
    right_total = sum(arr)
    left_total = 0

    for number in arr:
        right_total -= number
        if right_total == left_total:
            return "YES"
        left_total += number
    return "NO"


print(sherlock_and_array([1, 1, 4, 1, 1]))

