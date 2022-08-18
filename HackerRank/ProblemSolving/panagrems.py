# Challenge Name: Panagrams
# Difficulty: Easy

def pangrams(sentence):
    sentence = sentence.lower().replace(' ', '')
    set_characters = set(list(sentence))

    return "pangram" if len(set_characters) == 26 else "not pangram"


print(pangrams('We promptly judged antique ivory buckles for the next prize'))
print(pangrams('We promptly judged antique ivory buckles for the prize'))