# Challenge Name: The Grid Search
# Difficulty: Intermediate
from typing import List


def grid_search(grid: List[str], pattern: List[str]) -> str:
    grid_length = len(grid)
    pattern_length = len(pattern)

    pattern_first_row = pattern[0]
    for i in range(grid_length - pattern_length + 1):
        grid_row = str(grid[i])
        if pattern_first_row in grid_row:
            for k in range(len(grid_row) - len(pattern_first_row) + 1):
                if grid_row[k:k + len(pattern_first_row)] == pattern_first_row:
                    for j in range(pattern_length):
                        if pattern[j] != grid[i + j][k:k + len(pattern_first_row)]:
                            break
                    else:
                        return "YES"

    return "NO"


G = ["7283455864",
     "6731158619",
     "8988242643",
     "3830589324",
     "2229505813",
     "5633845374",
     "6473530293",
     "7053106601",
     "0834282956",
     "4607924137"]

P = ["9505",
     "3845",
     "3530"]

print(grid_search(G, P))
