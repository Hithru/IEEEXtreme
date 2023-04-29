# Problem Number: 13
# Problem Name: Roman to Integer
# Difficulty: Easy

class Solution:
    def romanToInt(self, s: str) -> int:
        conversion = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
            "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900
        }
        value = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1 and s[i:i+2] in conversion:
                value += conversion[s[i:i+2]]
                i += 2
            else:
                value += conversion[s[i]]
                i += 1
        return value
