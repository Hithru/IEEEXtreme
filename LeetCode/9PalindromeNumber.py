# Problem Number: 9
# Problem Name: Palindrome Number
# Difficulty: Easy

from typing import List


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

