# Challenge Name: Grid Challenge
# Difficulty: Easy
from typing import List


def gird_challenge(grid: List[str]):
    column_grid = [""] * len(grid[0])

    for i in range(len(grid)):
        row = grid[i]
        new_row = "".join(sorted(row))
        grid[i] = new_row

        for k in range(len(new_row)):
            column_grid[k] += new_row[k]

    for column in column_grid:
        sorted_column = "".join(sorted(column))
        if column != sorted_column:
            return "NO"
    return "YES"


print(gird_challenge(['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']))
