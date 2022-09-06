# Challenge Name: Morgan And String
# Difficulty: Expert

def morgan_and_string(str1: str, str2: str):
    i = 0
    j = 0
    answer = ""
    while True:
        if i == len(str1):
            answer += str2[j:]
            break
        if j == len(str2):
            answer += str1[i:]
            break
        if str1[i] < str2[j]:
            answer += str1[i]
            i += 1
        elif str2[j] < str1[i]:
            answer += str2[j]
            j += 1
        elif str1[i] == str2[j]:
            k = 0
            first_string = True
            while i + k < len(str1) and j + k < len(str2) and str1[i + k] == str2[j + k]:
                k += 1

            if i + k == len(str1) or j + k == len(str2) or str1[i + k] <= str2[j + k]:
                answer += str1[i]
                i += 1
            else:
                answer += str2[j]
                j += 1
    return answer


print(morgan_and_string("hello", "world"))
print(morgan_and_string("hi", "world"))