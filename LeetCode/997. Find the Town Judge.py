# Problem Number: 997
# Problem Name: Find the Town Judge
# Difficulty: Easy
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        if n == 1 and len(trust) == 0:
            return 1
        trust_one = {}
        trustes = {}

        for tup in trust:
            trust_one[tup[0]] = True
            trustes.setdefault(tup[1], set())
            trustes[tup[1]].add(tup[0])
            trust_one.setdefault(tup[1], False)

        answer = []
        for k, v in trust_one.items():
            if v == False:
                answer.append(k)
                if len(answer) > 1:
                    return -1

        if len(answer) == 0:
            return -1
        else:
            if len(trustes[answer[0]]) == n - 1:
                return answer[0]
            else:
                return -1