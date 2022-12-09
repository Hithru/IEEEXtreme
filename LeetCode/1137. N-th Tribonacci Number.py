# Problem Number: 1137
# Problem Name: N-th Tribonacci Number
# Difficulty: Easy
class Solution:
    tribonacci_dict = {0:0,1:1,2:1}
    def tribonacci(self, n: int) -> int:

        if n in self.tribonacci_dict:
            return self.tribonacci_dict[n]
        else:
            answer = self.tribonacci(n-1) + self.tribonacci(n-2)+ self.tribonacci(n-3)
            self.tribonacci_dict[n] = answer
            return answer