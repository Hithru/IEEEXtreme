# Problem Number: 198
# Problem Name: House Robber
# Difficulty: Medium
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        table = {len(nums)+1:0,len(nums):0}
        def robHouse(index):
            if index in table:
                return table[index]
            else:
                take = nums[index] + robHouse(index+2)
                leave = robHouse(index+1)
                answer = max(take,leave)

                table[index] = answer
                return answer

        return robHouse(0)