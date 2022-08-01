# Challenge Name: Cavity Map
# Difficulty: Easy

def cavity_map(grid):
    n = len(grid)
    int_grid = []
    ans_grid = []
    for row in grid:
        row = [int(letter) for letter in row]
        int_grid.append(row)

    ans_grid.append([str(i) for i in int_grid[0]])
    for i in range(1, n - 1):
        ans_row = [str(int_grid[i][0])]
        for num in range(1, n - 1):
            if int_grid[i][num] > int_grid[i][num - 1] and int_grid[i][num] > int_grid[i][num + 1] and int_grid[i][
                num] > int_grid[i + 1][num] and int_grid[i][num] > int_grid[i - 1][num]:
                ans_row.append('X')
            else:
                ans_row.append(str(int_grid[i][num]))
        ans_row.append(str(int_grid[i][n - 1]))
        ans_grid.append(ans_row)
    if n > 1:
        ans_grid.append([str(i) for i in int_grid[n - 1]])
    return ["".join(row) for row in ans_grid]


print(cavity_map(['989', '191', '111']))
