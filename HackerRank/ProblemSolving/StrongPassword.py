# Challenge Name: Strong Password
# Difficulty: Easy

def minimum_characters_needed(password: str) -> int:
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    characters_needed = 4
    upper_case_needed = True
    lower_case_needed = True
    special_character_needed = True
    number_needed = True
    for c in password:
        if upper_case_needed and c in upper_case:
            characters_needed -= 1
            upper_case_needed = False
        if lower_case_needed and c in lower_case:
            characters_needed -= 1
            lower_case_needed = False
        if special_character_needed and c in special_characters:
            characters_needed -= 1
            special_character_needed = False
        if number_needed and c in numbers:
            characters_needed -= 1
            number_needed = False

    if len(password) < 6 and 6 - len(password) > characters_needed:
        characters_needed = 6 - len(password)
    return characters_needed


print(minimum_characters_needed("Ab1"))
print(minimum_characters_needed("#HackerRank"))
