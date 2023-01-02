# Problem Number: 520
# Problem Name: Detect Capital
# Difficulty: Easy
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word == word.upper() or word == word.lower() or word == word.capitalize():
            return True
        else:
            return False