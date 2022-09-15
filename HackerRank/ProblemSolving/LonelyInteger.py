# Challenge Name: Lonely Integer
# Difficulty: Easy
from typing import List


def lonely_integer(numbers: List[int]):
    counts = {}
    for number in numbers:
        counts.setdefault(number, 0)
        counts[number] += 1

    for k, v in counts.items():
        if v == 1:
            return k


print(lonely_integer([0, 0, 1, 2, 1]))
