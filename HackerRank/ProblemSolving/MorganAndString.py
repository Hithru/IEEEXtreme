# Challenge Name: Morgan And String
# Difficulty: Expert

def morgan_and_string(string1: str, string2: str):
    i = 0
    j = 0
    length_string1 = len(string1)
    length_string2 = len(string2)
    string1 = string1 + "z"
    string2 = string2 + "z"
    answer = ""
    while True:
        if i == length_string1:
            answer += string2[j:-1:]
            break
        if j == length_string2:
            answer += string1[i:-1:]
            break
        if string1[i] < string2[j]:
            answer += string1[i]
            i += 1
        elif string2[j] < string1[i]:
            answer += string2[j]
            j += 1
        elif string1[i] == string2[j]:

            if string1[i::] < string2[j::]:
                answer += string1[i]
                i += 1
            else:
                answer += string2[j]
                j += 1
    return answer


print(morgan_and_string("hello", "world"))
print(morgan_and_string("hi", "world"))
