# Problem Number: 7
# Problem Name: Reverse Integers
# Difficulty: Medium

class Solution:
    def reverse(self, x: int) -> int:

        if x > 2 ** 31 - 1 or x < -2 ** 31:
            return 0
        string_x = str(abs(x))
        if x >= 0:

            answer = int(string_x[::-1])
        else:
            answer = -int(string_x[::-1])
        if answer > 2 ** 31 - 1 or answer < -2 ** 31:
            return 0

        return answer