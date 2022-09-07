# Challenge Name: Missing Numbers
# Difficulty: Easy

def missing_numbers(arr, brr):
    characters = {}
    for i in arr:
        characters.setdefault(i, 0)
        characters[i] += 1
    answer = []
    print(characters)
    for j in brr:
        if j in characters:
            if characters[j] == 0:
                characters[j] = -1
                answer.append(j)
            else:
                characters[j] -= 1

        else:
            answer.append(j)
            characters[j] = -1
    print(characters)
    return sorted(answer)


print(missing_numbers([203, 204, 205, 206, 207, 208, 203, 204, 205, 206],
                      [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]))
