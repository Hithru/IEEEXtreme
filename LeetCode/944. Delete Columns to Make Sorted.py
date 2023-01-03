# Problem Number: 944
# Problem Name: Delete Columns to Make Sorted
# Difficulty: Easy
from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        if len(strs) == 0:
            return 0

        length = len(strs[0])
        answer = 0
        for i in range(length):
            new_word = ""
            for k in strs:
                new_word += k[i]

            if new_word != "".join(sorted(new_word)):
                answer += 1
        return answer