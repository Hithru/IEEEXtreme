# Challenge Name: Common Child
# Difficulty: Intermediate

def common_child(str1: str, str2: str):
    common_subsequence_length = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                common_subsequence_length[i + 1][j + 1] = common_subsequence_length[i][j] + 1

            else:
                common_subsequence_length[i + 1][j + 1] = max(
                    common_subsequence_length[i][j + 1], common_subsequence_length[i + 1][j])

    return common_subsequence_length[len(str1)][len(str2)]


print(common_child("hello", "world"))
print(common_child("hi", "world"))
