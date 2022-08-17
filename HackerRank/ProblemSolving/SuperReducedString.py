# Challenge Name: Super Reduced String
# Difficulty: Easy


def super_reduced_string(string: str) -> str:
    index = 1
    while True:
        if string[index] == string[index-1]:
            string = string[:index-1]+string[index+1:]
            if index != 1:
                index -= 1
        else:
            index +=1

        if len(string) == 0 or index == len(string):
            break
    return "Empty String" if len(string) == 0 else string



print(super_reduced_string("aaabccddd"))
print(super_reduced_string("aa"))
print(super_reduced_string("baab"))