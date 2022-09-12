# Challenge Name: Priyanka and Toys
# Difficulty: Easy
from typing import List


def priyanka_and_toys(weights: List[int]):
    weights.sort()
    first = weights[0]
    parts = 0

    i = 0
    while i < len(weights):
        if weights[i] - first <= 4:
            i += 1
        else:
            first = weights[i]
            parts += 1
            i += 1
    parts += 1
    return parts


print(priyanka_and_toys([1, 1, 4, 1, 1]))