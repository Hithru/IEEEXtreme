# Book : 7 Days with Dynamic Programming
# Problem : Longest Common SubString

# Sequence1 : ungenerous
# Sequence2 : genius
# Answer : gen

def longest_common_substring(str1: str, str2: str):
    common_substring_length = {(0, 0): 0}

    for i in range(len(str1)):

        for j in range(len(str2)):

            if str1[i] == str2[j]:
                if (i, j) in common_substring_length:
                    common_substring_length[(i + 1, j + 1)] = common_substring_length[(i, j)] + 1
                else:
                    common_substring_length[(i + 1, j + 1)] = 1

    maximum_key_value = max(common_substring_length.items(), key=lambda k: k[1])

    return str1[maximum_key_value[0][0] - maximum_key_value[1]:maximum_key_value[0][0]]


print(longest_common_substring("ungenerous", "genius"))
