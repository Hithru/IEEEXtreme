# Challenge Name: Two Strings
# Difficulty: Easy

def two_string(str1: str, str2: str):
    set1 = set(str1)
    set2 = set(str2)

    return "YES" if len(set1.intersection(set2)) > 0 else "NO"


print(two_string("hello", "world"))
print(two_string("hi", "world"))
