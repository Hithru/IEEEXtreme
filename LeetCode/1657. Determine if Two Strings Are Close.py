# Problem Number: 1657
# Problem Name: Determine if Two Strings Are Close
# Difficulty: Medium

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) == len(word2):
            word1_char = {}
            for i in word1:
                word1_char.setdefault(i, 0)
                word1_char[i] += 1

            word2_char = {}
            for j in word2:
                word2_char.setdefault(j, 0)
                word2_char[j] += 1

            if sorted(list(word1_char.values())) == sorted(list(word2_char.values())) and sorted(
                    list(word1_char.keys())) == sorted(list(word2_char.keys())):
                return True
            else:
                return False

        else:
            return False
