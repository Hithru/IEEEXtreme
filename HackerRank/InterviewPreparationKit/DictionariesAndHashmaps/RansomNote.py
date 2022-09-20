# Challenge Name: Ransom Note
# Difficulty: Easy

def checkMagazine(magazine, note) -> str:
    magazine_word = {}
    for word in magazine:
        magazine_word.setdefault(word, 0)
        magazine_word[word] += 1
    for word in note:
        if word not in magazine_word:
            return "No"
        else:
            if magazine_word[word] == 0:
                return "No"
            else:
                magazine_word[word] -= 1
    return "Yes"


print(checkMagazine(['give', 'me', 'one', 'grand', 'today', 'night'], ['give', 'one', 'grand', 'today']))
