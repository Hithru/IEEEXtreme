# Book : 7 Days with Dynamic Programming
# Problem : Longest Increasing Odd Even Subsequence

# sequence : [5, 6, 2, 1, 7, 4, 8, 3]
# Answer : [5, 6, 7, 8]
from typing import List


def longest_increasing_odd_even_subsequence(sequence: List[int]):
    sequence_details = {}

    for i in range(1, len(sequence)):
        sequence_details.setdefault(i, 1)
        for j in range(i):
            sequence_details.setdefault(j, 1)
            if (sequence[i] > sequence_details[j] and (sequence[i] + sequence[j]) % 2 != 0 and sequence_details[i] <
                    sequence_details[j] + 1):
                sequence_details[i] = sequence_details[j] + 1

    return max(sequence_details.items(), key=lambda k: k[1])


print(longest_increasing_odd_even_subsequence([5, 6, 2, 1, 7, 4, 8, 3]))
