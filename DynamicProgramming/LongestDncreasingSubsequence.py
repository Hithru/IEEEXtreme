# Book : 7 Days with Dynamic Programming
# Problem : Longest Decreasing Subsequence

# Given Set : 10, -1, 4, 7, 0, 5, 2, 1
# Answer : 10, 7, 5, 2, 99

from typing import List


def longest_decreasing_subsequence(sequence: List):
    decreasing_sequence_length = {0: 1}
    decreasing_sequence = [[sequence[0]]]
    for i in range(1, len(sequence)):
        decreasing_sequence_length[i] = 1
        decreasing_sequence.append([sequence[i]])
        for j in range(0, i):
            if sequence[i] < sequence[j] and decreasing_sequence_length[i] < decreasing_sequence_length[j] + 1:
                decreasing_sequence_length[i] = decreasing_sequence_length[j] + 1
                decreasing_sequence[i] = decreasing_sequence[j] + [sequence[i]]

    maximum_key_value = max(decreasing_sequence_length.items(), key=lambda k: k[1])

    return maximum_key_value[1], decreasing_sequence[maximum_key_value[0]]


print(longest_decreasing_subsequence([10, -1, 4, 7, 0, 5, 2, 1]))
