# Challenge Name: Davis' Stair Case
# Difficulty: Easy

ways_dictionary = {0: 1}


def stepPerms(number: int):
    if number in ways_dictionary:
        return ways_dictionary[number]
    elif number < 0:
        return 0
    else:
        num_ways = 0
        for i in [1, 2, 3]:
            num_ways += stepPerms(number - i)
        ways_dictionary[number] = num_ways
        return num_ways


n = int(input())
print(stepPerms(n))
