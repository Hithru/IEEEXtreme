# Problem Number: 740
# Problem Name: Delete and Earn
# Difficulty: Medium
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        n = max(nums) +1
        num_count = [0 for i in range(n)]
        print(num_count)

        for k in nums:
            num_count[k] +=1

        dp = [[0,0] for i in range(n)]

        for j in range(1,n):
            dp[j][0] = max(dp[j-1][0],dp[j-1][1])
            dp[j][1] = dp[j-1][0] + j * num_count[j]

        return max(dp[n-1][0],dp[n-1][1])