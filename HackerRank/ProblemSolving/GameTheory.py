# Challenge Name: Game Theory
# Difficulty: Easy
value_dict = {1: "Second", 2: "First", 3: "First", 4: "First", 5: "First", 6: "First"}


def gameOfStones(n: int):
    if n in value_dict:
        return value_dict[n]
    else:
        ans1 = gameOfStones(n - 2)
        ans2 = gameOfStones(n - 3)
        ans3 = gameOfStones(n - 5)
        if ans1 == "Second" or ans2 == "Second" or ans3 == "Second":
            value_dict[n] = "First"
        else:
            value_dict[n] = "Second"
        return value_dict[n]


print(gameOfStones(50))
