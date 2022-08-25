# Challenge Name: Making Anagrams
# Difficulty: Easy


def making_anagrams(string1: str, string2: str):
    characters_string1 = {}
    difference = 0
    for character in string1:
        characters_string1.setdefault(character, 0)
        characters_string1[character] += 1

    for character in string2:
        if character in characters_string1:
            characters_string1[character] -= 1
        else:
            difference += 1
    difference += sum([abs(i) for i in characters_string1.values() if i != 0])

    return difference


print(making_anagrams("cde", "abc"))
