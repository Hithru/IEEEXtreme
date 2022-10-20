import sys

sys.setrecursionlimit(1500)


def get_number_end(line, tile, end_right):
    new_line = lines[line]
    max_number = max(new_line)
    min_number = min(new_line)
    if end_right:
        if min_number >= tile:
            moves = max_number - tile
        else:
            moves = tile - min_number + max_number - min_number
    else:
        if max_number <= tile:
            moves = tile - min_number
        else:
            moves = max_number - min_number + max_number - tile
    return moves


def choose_best(n, k, tile):
    if (k, tile) in dynamic_list:
        return dynamic_list[(k, tile)]
    elif k == n - 1:
        dynamic_list[(k, tile)] = min(get_number_end(k, tile, True), get_number_end(k, tile, False))
        return dynamic_list[(k, tile)]
    else:
        new_line = lines[k]
        max_number = max(new_line)
        min_number = min(new_line)
        end_right = get_number_end(k, tile, True)
        end_left = get_number_end(k, tile, False)
        answer = min(end_right + choose_best(n, k + 1, max_number), end_left + choose_best(n, k + 1, min_number))
        dynamic_list[(k, tile)] = answer
        return answer


test_cases = int(input())
for i in range(test_cases):
    n, m = map(int, input().split())
    number_of_moves = 0
    dynamic_list = {}
    first_line = [int(i) for i in input().split()]
    number_of_moves = max(first_line)
    current_tile = max(first_line)
    lines = [[]]
    for j in range(n - 1):
        new_line = [int(i) for i in input().split()]
        lines.append(new_line)

    number_of_moves += choose_best(n, 1, current_tile)

    print(number_of_moves)

# Sample Input 0
#
# 1
# 2 3
# 3 1 2
# 2 5 3
# Sample Output 0
#
# 7