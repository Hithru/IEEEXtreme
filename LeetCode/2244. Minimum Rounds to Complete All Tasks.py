# Problem Number: 2244
# Problem Name: Minimum Rounds to Complete All Tasks
# Difficulty: Medium
from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:

        tasks_count = {}
        for t in tasks:
            tasks_count.setdefault(t, 0)
            tasks_count[t] += 1

        answer = 0
        for k, v in tasks_count.items():
            if v == 1:
                return -1
            else:
                answer += (v // 3)
                if v % 3 > 0:
                    answer += 1
        return answer