# Challenge Name: Pairs
# Difficulty: Medium
from typing import List


def pairs(target_value: int, arr: List[int]):
    answer = 0
    arr_dict = {j: True for j in arr}

    for i in arr:
        if i + target_value in arr_dict:
            answer += 1
        if i - target_value in arr_dict:
            answer += 1
    return answer // 2


print(pairs(2, [1, 5, 3, 4, 2]))
