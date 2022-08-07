# Book : 7 Days with Dynamic Programming
# Problem : Longest Increasing Subsequence

# Given Set : 1, 9, 19, 17, 32, 15, 99
# Answer : 1, 9, 17, 32, 99

from typing import List


def longest_increasing_subsequence(sequence: List):
    increasing_sequence_length = {0: 1}
    increasing_sequence = [[sequence[0]]]
    for i in range(1, len(sequence)):
        increasing_sequence_length[i] = 1
        increasing_sequence.append([sequence[i]])
        for j in range(0, i):
            if sequence[i] > sequence[j] and increasing_sequence_length[i] < increasing_sequence_length[j] + 1:
                increasing_sequence_length[i] = increasing_sequence_length[j] + 1
                increasing_sequence[i] = increasing_sequence[j] + [sequence[i]]

    maximum_key_value = max(increasing_sequence_length.items(), key=lambda k: k[1])

    return maximum_key_value[1], increasing_sequence[maximum_key_value[0]]


print(longest_increasing_subsequence([1, 9, 19, 17, 32, 15, 99]))
