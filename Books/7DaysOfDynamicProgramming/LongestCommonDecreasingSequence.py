# Book : 7 Days with Dynamic Programming
# Problem : Longest Common Decreasing Subsequence

# Sequence1 : 9, 4, 6, 2
# Sequence2 : 6, 9, 7, 2, 4, 3
# Answer : 9, 2

from typing import List


def longest_common_decreasing_subsequence(sequence1: List, sequence2: List):
    common_decreasing_sequence_length = {i: 0 for i in range(len(sequence2))}
    common_decreasing_sequence = [[] for i in range(len(sequence2))]

    for i in range(len(sequence1)):
        current = 0
        current_sequence = []
        for j in range(len(sequence2)):
            if sequence1[i] == sequence2[j]:
                if common_decreasing_sequence_length[j] > current + 1:
                    current_sequence = common_decreasing_sequence[j]
                else:
                    current_sequence.append(sequence2[j])
                    common_decreasing_sequence[j] = current_sequence

                common_decreasing_sequence_length[j] = max(current + 1, common_decreasing_sequence_length[j])

            if sequence1[i] < sequence2[j]:
                if common_decreasing_sequence_length[j] >= current:
                    current_sequence = common_decreasing_sequence[j][::]
                current = max(current, common_decreasing_sequence_length[j])

    maximum_key_value = max(common_decreasing_sequence_length.items(), key=lambda k: k[1])

    return maximum_key_value[1], common_decreasing_sequence[maximum_key_value[0]]


print(longest_common_decreasing_subsequence([9, 4, 6, 2], [6, 9, 7, 2, 4, 3]))
