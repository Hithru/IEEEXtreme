# Challenge Name: Sherlock and Valid String
# Difficulty: Medium

def isValid(s):
    dic_char = {}

    for i in s:
        if i in dic_char:
            dic_char[i] += 1
        else:
            dic_char[i] = 1

    values = list(dic_char.values())
    minimum_value = min(values)
    maximum_value = max(values)

    minimum_count = values.count(minimum_value)
    maximum_count = values.count(maximum_value)

    if minimum_value == maximum_value:
        return "YES"
    elif (maximum_value - minimum_value) <= 1 and (maximum_count == 1 or minimum_count == 1):
        return "YES"
    elif (minimum_count + maximum_count == len(values)) and minimum_value == 1 and minimum_count == 1:
        return "YES"
    else:
        return "NO"


print(isValid('abcdefghhgfedecba'))
