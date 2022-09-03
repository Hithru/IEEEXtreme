# Challenge Name: Anagrams
# Difficulty: Easy

def encryption(string:str):
    if len(string) % 2 == 1:
        return -1
    string1 = string[:len(string) // 2]
    string2 = string[len(string) // 2:]
    characters = {}
    answer = 0
    for i in string1:
        characters.setdefault(i, 0)
        characters[i] += 1
    for j in string2:
        if j in characters:
            characters[j] -= 1
            if characters[j] == 0:
                del characters[j]
        else:
            answer += 1

    return answer


print(encryption('aaabbb'))
print(encryption('xaxbbbxx'))
print(encryption('abc'))