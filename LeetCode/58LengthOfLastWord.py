# Problem Number: 58
# Problem Name: Length Of Last Word
# Difficulty: Easy

class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        return len(s.strip().split()[-1])