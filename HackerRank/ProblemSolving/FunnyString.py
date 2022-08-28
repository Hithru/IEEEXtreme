# Challenge Name: Funny String
# Difficulty: Easy

def funny_string(string: str) -> str:
    reverse_string = string[::-1]
    for i in range(1, len(string)):
        if abs(ord(string[i]) - ord(string[i - 1])) != abs(ord(reverse_string[i]) - ord(reverse_string[i - 1])):
            return "Not Funny"
    return "Funny"


print(funny_string('acxz'))
print(funny_string('bcxz'))
