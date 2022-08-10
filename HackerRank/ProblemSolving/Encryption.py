# Challenge Name: Encryption
# Difficulty: Intermediate

def encryption(s):
    modified_string = s.replace(" ", "")
    length = len(modified_string)
    sqrt_length = length ** 0.5
    column = int(sqrt_length)
    if sqrt_length > int(sqrt_length):
        column += 1

    answer = ["" for i in range(column)]

    for i in range(len(modified_string)):
        answer[i % column] += modified_string[i]

    return " ".join(answer)


print(encryption('haveaniceday'))
print(encryption('feedthedog'))
print(encryption('chillout'))