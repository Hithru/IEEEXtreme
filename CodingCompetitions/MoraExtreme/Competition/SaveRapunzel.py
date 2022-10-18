def get_number(k, tile):
    scope_tile = tile
    moves = 0
    new_line = lines[k]
    max_number = max(new_line)
    min_number = min(new_line)
    if max_number > scope_tile:

        if min_number >= scope_tile:
            moves += (max_number - scope_tile)
            scope_tile = max_number
        else:
            number_of_moves_to_right = max_number - scope_tile
            number_of_moves_to_left = scope_tile - min_number
            if number_of_moves_to_left > number_of_moves_to_right:
                moves += (number_of_moves_to_right + max_number - min_number)
                scope_tile = min_number
            elif number_of_moves_to_left < number_of_moves_to_right:
                moves += (number_of_moves_to_left + max_number - min_number)
                scope_tile = max_number
            else:
                go_left = True
                if k != n - 2:
                    next_line = lines[k + 1]
                    next_max_number = max(next_line)
                    next_min_number = min(next_line)
                    if get_number(k + 1, max_number) > get_number(k + 1, min_number):
                        go_left = False
                if go_left:
                    moves += (number_of_moves_to_left + max_number - min_number)
                    scope_tile = max_number
                else:
                    moves += (number_of_moves_to_right + max_number - min_number)
                    scope_tile = min_number

    else:
        moves += (scope_tile - min_number)
        scope_tile = min_number
    return moves, scope_tile


test_cases = int(input())
for i in range(test_cases):
    n, m = map(int, input().split())
    number_of_moves = 0
    first_line = [int(i) for i in input().split()]
    number_of_moves = max(first_line)
    current_tile = max(first_line)
    lines = []
    for j in range(n - 1):
        new_line = [int(i) for i in input().split()]
        lines.append(new_line)
    for k in range(n - 1):
        new_moves, tile = get_number(k, current_tile)
        number_of_moves += new_moves
        current_tile = tile

    print(number_of_moves)
