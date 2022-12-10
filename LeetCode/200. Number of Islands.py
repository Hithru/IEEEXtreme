# Problem Number: 200
# Problem Name: Number of Islands
# Difficulty: Medium
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_coloms = len(grid[0])
        num_rows = len(grid)
        traveled = [[False for i in range(num_coloms)] for j in range(num_rows)]

        lands = 0

        def explore(r,c):
            if grid[r][c] == "1":
                traveled[r][c] = True
                if r+1 < num_rows and not traveled[r+1][c]:
                    explore(r+1,c)
                if r-1 >= 0 and not traveled[r-1][c]:
                    explore(r-1,c)

                if c+1 < num_coloms and not traveled[r][c+1]:
                    explore(r,c+1)
                if c-1 >= 0 and not traveled[r][c-1]:
                    explore(r,c-1)
            else:
                return
        for i in range(num_rows):
            for j in range(num_coloms):
                if traveled[i][j]:
                    continue
                elif grid[i][j] == "1":
                    lands +=1
                    explore(i,j)
                else:
                    traveled[i][j] = True
        print(traveled)
        return lands
