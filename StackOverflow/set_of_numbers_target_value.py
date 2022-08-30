def nearest_target_sum(target_value, values):
    possible_values = {0: []}
    solution_indexes = {0: []}
    max_value_possible = 0
    values_to_be_handled = [0]
    while values_to_be_handled:
        value = values_to_be_handled.pop(0)
        solution = possible_values[value]
        solution_index = solution_indexes[value]
        if value == target_value:
            return value

        if value > max_value_possible:
            max_value_possible = value

        for i in range(len(values)):
            if i in solution_index:
                continue
            val = values[i]
            next_value = value + val
            if next_value > target_value:
                continue
            if next_value not in possible_values:
                possible_values[next_value] = solution + [val]
                solution_indexes[next_value] = solution_index + [i]
                values_to_be_handled.append(next_value)

    return max_value_possible, possible_values[max_value_possible]


print(nearest_target_sum(105, [60, 50, 50, 30, 20]))
print(nearest_target_sum(200, [60, 50, 50, 30, 20]))
