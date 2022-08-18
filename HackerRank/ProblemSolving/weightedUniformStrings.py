# Challenge Name: Weighted Uniform String
# Difficulty: Easy
from typing import List


def weighted_uniform_strings(s: str, queries: List[int]) -> List[str]:
    weights = set([ord(s[0]) - 96])

    consecutive_sum = ord(s[0]) - 96
    consecutive = True

    for i in range(1, len(s)):
        weight = ord(s[i]) - 96
        if s[i] == s[i - 1]:
            consecutive_sum += weight
            weights.add(consecutive_sum)
        else:
            consecutive_sum = weight
        weights.add(weight)

    answer = []
    return ["Yes" if number in weights else "No" for number in queries]


print(weighted_uniform_strings("abccddde", [1, 3, 12, 5, 9, 10]))
