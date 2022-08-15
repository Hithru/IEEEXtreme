# Challenge Name: Knapsack
# Difficulty: Medium

def knapsack(target_value, values):
    possible_values = {0: True}
    max_value_possible = 0
    values_to_be_handled = [0]
    while values_to_be_handled:
        value = values_to_be_handled.pop(0)
        if value == target_value:
            return value

        if value > max_value_possible:
            max_value_possible = value

        for val in values:
            next_value = value + val
            if next_value > target_value:
                continue
            if next_value not in possible_values:
                possible_values[next_value] = True
                values_to_be_handled.append(next_value)
    return max_value_possible


print(knapsack(9, [3, 4, 4, 4, 8]))
print(knapsack(11, [3, 7, 9]))
