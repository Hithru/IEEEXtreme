# Problem Number: 1
# Problem Name: Two Sum
# Difficulty: Easy

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int):
        dict = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if nums[i] in dict.keys():
                return [dict[nums[i]], i]
            else:
                dict[target - nums[i]] = i
        return None
