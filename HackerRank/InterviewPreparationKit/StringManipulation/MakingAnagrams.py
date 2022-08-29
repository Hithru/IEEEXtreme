# Challenge Name: Making Anagrams
# Difficulty: Easy

def making_anagrams(string1: str, string2: str) -> int:
    characters = {}
    for i in string1:
        characters.setdefault(i, 0)
        characters[i] += 1
    for j in string2:
        characters.setdefault(j, 0)
        characters[j] -= 1

    return sum([abs(i) for i in characters.values()])


print(making_anagrams('cde', 'abc'))
