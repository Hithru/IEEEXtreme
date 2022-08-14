# Book : 7 Days with Dynamic Programming
# Problem : Longest Common SubSequence

# Sequence1 : opengenus
# Sequence2 : engineers
# Answer : 5 ( "engns" or "enges" )

def longest_common_subsequence(str1: str, str2: str):
    common_subsequence_length = {(0, 0): 0, (0, 1): 0, (1, 0): 0}

    for i in range(1,len(str1)+1):
        common_subsequence_length[(i,0)] = 0
    for j in range(1,len(str2)+1):
        common_subsequence_length[(0,j)] = 0

    for i in range(len(str1)):

        for j in range(len(str2)):

            if str1[i] == str2[j]:
                common_subsequence_length[(i + 1, j + 1)] = common_subsequence_length[(i, j)] + 1

            else:
                common_subsequence_length[(i + 1, j + 1)] = max(
                    common_subsequence_length[(i, j + 1)], common_subsequence_length[(i + 1, j)])
    maximum_key_value = max(common_subsequence_length.items(), key=lambda k: k[1])

    print(common_subsequence_length)
    return maximum_key_value


print(longest_common_subsequence("opengenus", "engineers"))
