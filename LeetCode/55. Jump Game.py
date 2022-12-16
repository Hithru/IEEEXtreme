# Problem Number: 55
# Problem Name: Jump Game
# Difficulty: Medium
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        max_num = nums[0]
        if max_num >= len(nums) - 1:
            return True
        for i in range(1, len(nums)):
            if i > max_num:
                return False
            new_best = i + nums[i]
            if new_best > max_num:
                max_num = new_best

            if max_num >= len(nums) - 1:
                return True

        return False