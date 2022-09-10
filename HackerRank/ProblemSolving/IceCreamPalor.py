# Challenge Name: Ice Cream Parlor
# Difficulty: Easy
from typing import List


def ice_cream_parlor(m: int, arr: List[int]) -> List[int]:
    difference = {}
    for index, value in enumerate(arr):
        if value in difference:
            return [difference[value], index + 1]

        difference[m - value] = index + 1


print(ice_cream_parlor(5, [1, 4, 5, 3, 2]))
