# Challenge Name: Strange Counter
# Difficulty: Easy
import math


def strange_counter(time: int):
    number_of_three_multiplies = math.ceil(time / 3)
    power_of_two_value = math.floor(math.log2(number_of_three_multiplies))
    two_power_value = 2 ** power_of_two_value
    next_round_value = 3 * 2 ** power_of_two_value

    answer = next_round_value - (time - 1 - 3 * (two_power_value - 1))
    return answer


print(strange_counter(4))
print(strange_counter(17))
