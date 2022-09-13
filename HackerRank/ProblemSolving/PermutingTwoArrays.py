# Challenge Name: Permuting Two Arrays
# Difficulty: Easy
from typing import List


def permuting_two_arrays(k: int, A: List[int], B: List[int]):
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        if A[i] + B[i] < k:
            return "NO"
    return "YES"


print(permuting_two_arrays(1, [2, 1, 3], [7, 8, 9]))
