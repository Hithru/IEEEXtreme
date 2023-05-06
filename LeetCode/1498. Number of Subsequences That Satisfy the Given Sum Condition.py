# Problem Number: 1498
# Problem Name: Number of Subsequences That Satisfy the Given Sum Condition
# Difficulty: Medium

from typing import List

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        MOD = 10**9 + 7
        res = 0
        left, right = 0, len(nums) - 1

        powers_of_two = [1] * len(nums)
        for i in range(1, len(nums)):
            powers_of_two[i] = powers_of_two[i-1] * 2 % MOD

        while left <= right:
            if nums[left] + nums[right] <= target:
                res += powers_of_two[right - left]
                res %= MOD
                left += 1
            else:
                right -= 1

        return res

