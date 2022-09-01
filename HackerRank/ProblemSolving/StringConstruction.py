# Challenge Name: String Construction
# Difficulty: Easy

def string_construction(string: str) -> str:
    return len(set(string))


print(string_construction('abcd'))
print(string_construction('abab'))