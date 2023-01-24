# Problem Number: 118
# Problem Name: Pascal's Triangle
# Difficulty: Easy
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        answer = [[1],[1,1]]

        for i in range(2,numRows):
            newRow = [answer[i-1][0]]
            for k in range(len(answer[i-1])-1):
                newRow.append(answer[i-1][k]+answer[i-1][k+1])
            newRow.append(answer[i-1][-1])
            answer.append(newRow)

        return answer[:numRows]