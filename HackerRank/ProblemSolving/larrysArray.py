# Challenge Name: Larrys Array
# Difficulty: Intermediate
from typing import List


def larry_array(array: List):
    unsorted_swaps, num_swaps = len(array) - 1, 0
    swaps = True
    while swaps:
        swaps = False
        for i in range(0, unsorted_swaps):
            if array[i + 1] < array[i]:
                array[i + 1], array[i] = array[i], array[i + 1]
                num_swaps += 1
                swaps = True
        unsorted_swaps -= 1

    if num_swaps % 2 == 0:
        return "YES"
    return "NO"


print(larry_array([1, 3, 4, 2]))
print(larry_array([1, 2, 3, 5, 4]))
print(larry_array([3, 1, 2]))
