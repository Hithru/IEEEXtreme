# Book : 7 Days with Dynamic Programming
# Problem : Longest Increasing Subsequence

# Sequence1 : 2, 6, 4, 9
# Sequence2 : 3, 4, 2, 7, 9, 6
# Answer : 2, 9

from typing import List


def longest_common_increasing_subsequence(sequence1: List, sequence2: List):
    common_increasing_sequence_length = {i: 0 for i in range(len(sequence2))}
    common_increasing_sequence = [[] for i in range(len(sequence2))]

    for i in range(len(sequence1)):
        current = 0
        current_sequence = []
        for j in range(len(sequence2)):
            if sequence1[i] == sequence2[j]:
                if common_increasing_sequence_length[j] >= current + 1:
                    current_sequence = common_increasing_sequence[j]
                else:
                    current_sequence.append(sequence2[j])
                    common_increasing_sequence[j] = current_sequence

                common_increasing_sequence_length[j] = max(current + 1, common_increasing_sequence_length[j])

            if sequence1[i] > sequence2[j]:
                if common_increasing_sequence_length[j] >= current:
                    current_sequence = common_increasing_sequence[j][::]
                current = max(current, common_increasing_sequence_length[j])

    maximum_key_value = max(common_increasing_sequence_length.items(), key=lambda k: k[1])

    return maximum_key_value[1], common_increasing_sequence[maximum_key_value[0]]


print(longest_common_increasing_subsequence([2, 6, 4, 9], [3, 4, 2, 7, 9, 6]))
