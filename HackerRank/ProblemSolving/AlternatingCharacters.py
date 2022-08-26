# Challenge Name: Alternating Characters
# Difficulty: Easy

def alternating_characters(string: str):
    answer = 0

    answer_string = string[0]
    for i in range(1, len(string)):
        if answer_string[-1] == string[i]:
            answer += 1
        else:
            answer_string += string[i]
    return answer


print(alternating_characters("ABABABAB"))
print(alternating_characters("AAABBB"))
