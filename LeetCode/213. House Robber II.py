# Problem Number: 213
# Problem Name: House Robber ii
# Difficulty: Medium
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        def robHouse(index, nums, table):
            if index in table:
                return table[index]
            else:
                take = nums[index] + robHouse(index + 2, nums, table)
                leave = robHouse(index + 1, nums, table)
                answer = max(take, leave)

                table[index] = answer
                return answer

        print(len(nums), len(nums[:-1]))
        if len(nums) == 1:
            return nums[0]
        else:
            table1 = {len(nums[:-1:]) + 1: 0, len(nums[:-1:]): 0}
            takeFirst = robHouse(0, nums[:len(nums):], table1)

            table2 = {len(nums) + 1: 0, len(nums): 0}
            leaveFirst = robHouse(1, nums, table2)

            return max(takeFirst, leaveFirst)