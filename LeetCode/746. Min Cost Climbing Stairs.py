# Problem Number: 746
# Problem Name: Min Cost Climbing Stairs
# Difficulty: Easy
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        height = len(cost)
        table = {height: 0}

        def climb(current_index):
            if current_index == height:
                return 0
            elif current_index in table:
                return table[current_index]
            else:
                one_from_current = cost[current_index] + climb(current_index + 1)
                answer = one_from_current
                if current_index + 1 < height:
                    two_from_current = cost[current_index] + climb(current_index + 2)

                    answer = min(one_from_current, two_from_current)
                table[current_index] = answer

                return answer

        min_cost = min(climb(0), climb(1))
        return min_cost