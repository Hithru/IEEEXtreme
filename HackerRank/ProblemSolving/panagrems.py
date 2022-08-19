# Challenge Name: Two Characters
# Difficulty: Easy

def two_characters(string: str):
    unique_string_characters = list(set(string))
    max_alternative_count = 0
    for x in range(len(unique_string_characters)):
        for y in range(x + 1, len(unique_string_characters)):
            case = [z for z in string if z == unique_string_characters[x] or z == unique_string_characters[y]]
            if len(set(case[::2])) == 1 and len(set(case[1::2])) == 1:
                max_alternative_count = max(len(case), max_alternative_count)
    return max_alternative_count


print(two_characters('beabeefeab'))
