# Challenge Name: Hacker Rank in String
# Difficulty: Intermediate

def hackerrank_in_string(string: str):
    hackerrank_string = "hackerrank"
    index = 0
    for character in string:
        if character == hackerrank_string[index]:
            index += 1
        if index == len(hackerrank_string):
            return "YES"
    return "NO"


print(hackerrank_in_string('hereiamstackerrank'))
print(hackerrank_in_string('hackerworld'))
print(hackerrank_in_string('hhaacckkekraraannk'))
