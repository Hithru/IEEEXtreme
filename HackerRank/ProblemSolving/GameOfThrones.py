# Challenge Name: Game of Thrones
# Difficulty: Easy

def game_of_thrones(string: str) -> str:
    characters = {}

    for char in string:
        characters.setdefault(char, 0)
        characters[char] += 1

    return "YES" if len([value for value in characters.values() if value % 2 != 0]) < 2 else "NO"


print(game_of_thrones('aaabbbb'))
print(game_of_thrones('cdefghmnopqrstuvw'))
