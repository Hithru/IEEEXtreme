# Problem Number: 1143
# Problem Name: Longest Common Subsequence
# Difficulty: Medium
class Solution:
    def longestCommonSubsequence(self, str1: str, str2: str) -> int:
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

        print(common_subsequence_length)
        return common_subsequence_length[(len(str1),len(str2))]