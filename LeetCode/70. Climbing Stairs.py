# Problem Number: 70
# Problem Name: Climbing Stairs
# Difficulty: Easy

class Solution:
    ways = {0:0,1:1,2:2}
    def climbStairs(self, n: int) -> int:

        if n in self.ways:
            return self.ways[n]
        else:
            answer = self.climbStairs(n-1)+self.climbStairs(n-2)
            self.ways[n] = answer

            return answer