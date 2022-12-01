# Problem Number: 1704
# Problem Name: Determine if String Halves Are Alike
# Difficulty: Easy
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        n = len(s)
        vowels = 0

        for i in range(n):
            if i < n // 2:
                if s[i] in ['a', 'e', 'i', 'o', 'u']:
                    vowels += 1
            else:
                if s[i] in ['a', 'e', 'i', 'o', 'u']:

                    if vowels == 0:
                        return False
                    else:
                        vowels -= 1
        if vowels > 0:
            return False
        else:
            return True
