# Challenge Name: Sherlock and Beast
# Difficulty: Easy


def sherlock_and_beast(number: int):
    number_fives = number // 3
    for k in range(number_fives, -1, -1):

        if (number - k * 3) % 5 == 0:
            return 3 * k * "5" + (number - k * 3) * "3"
    return "-1"


print(sherlock_and_beast(1))
print(sherlock_and_beast(11))
