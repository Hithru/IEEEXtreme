# Problem Number: 3
# Problem Name: Longest Substring Without Repeating Characters
# Difficulty: Medium

from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        for i in range(len(s)):
            string_now = s[i:]
            already_string = {}
            length = 0
            for k in string_now:
                if k in already_string:
                    break
                else:
                    already_string[k] = True
                    length +=1
            if length > max_length:
                max_length = length
        return max_length

