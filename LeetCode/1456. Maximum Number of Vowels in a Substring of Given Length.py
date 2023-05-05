# Problem Number: 1456
# Problem Name: Maximum number of Vowels in Substring
# Difficulty: Medium

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def is_vowel(c):
            return c in {'a', 'e', 'i', 'o', 'u'}

        max_vowels = current_vowels = sum(is_vowel(c) for c in s[:k])

        for i in range(k, len(s)):
            if is_vowel(s[i - k]):
                current_vowels -= 1
            if is_vowel(s[i]):
                current_vowels += 1
            max_vowels = max(max_vowels, current_vowels)

        return max_vowels
