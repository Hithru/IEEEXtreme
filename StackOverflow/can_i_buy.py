def can_i_buy(target_value, values):
    possible_values = {0: True}
    values_to_be_handled = [0]

    while values_to_be_handled:
        value = values_to_be_handled.pop(0)
        if value == target_value:
            return True
        for val in values:
            next_value = value + val
            if next_value > target_value:
                continue
            if next_value not in possible_values:
                possible_values[next_value] = True
                values_to_be_handled.append(next_value)

    return None



print(can_i_buy(24, [7, 9, 11]))
print(can_i_buy(23, [7, 9, 11]))
print(can_i_buy(7, [7, 9, 11]))
print(can_i_buy(14, [7, 9, 11]))
