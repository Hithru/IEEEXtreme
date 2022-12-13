# Problem Number: 931
# Problem Name: Minimum Falling Path Sum
# Difficulty: Medium
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        num_rows = len(matrix)
        num_coloms = len(matrix[0])
        table = {}
        def takeMinPath(i,j):
            answer = 0
            if (i,j) in table:
                return table[(i,j)]
            elif i == num_rows-1:
                table[(i,j)] = matrix[i][j]
                return matrix[i][j]
            else:

                if j==0:
                    answer = matrix[i][j] + min(takeMinPath(i+1,j+1),takeMinPath(i+1,j))
                elif j== num_coloms -1:
                    answer = matrix[i][j] + min(takeMinPath(i+1,j-1),takeMinPath(i+1,j))
                else:
                    answer = matrix[i][j] + min(takeMinPath(i+1,j-1),takeMinPath(i+1,j+1),takeMinPath(i+1,j))
                table[(i,j)] = answer
                return answer
        final_answer = float('inf')

        for k in range(num_coloms):
            value = takeMinPath(0,k)
            if value < final_answer:
                final_answer = value
        print("table",table)
        return final_answer
