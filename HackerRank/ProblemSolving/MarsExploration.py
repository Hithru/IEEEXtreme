# Challenge Name: Mars Exploration
# Difficulty: Easy


def mars_exploration(string: str) -> int:
    change = 0
    index = 0
    while index < len(string):
        if (index % 3 == 2 or index % 3 == 0) and string[index] != "S":
            change += 1
        elif index % 3 == 1 and string[index] != "O":
            change += 1

        index += 1
    return change



print(mars_exploration("SOSSPSSQSSOR"))
print(mars_exploration("SOSSOT"))
