# Challenge Name: Beautiful Binary String
# Difficulty: Easy

def beautiful_binary_string(binary_string: str):
    steps_needed = 0
    array_string = list(binary_string)
    for i in range(len(binary_string) - 2):
        if array_string[i] == "0" and array_string[i + 1] == "1" and array_string[i + 2] == "0":
            steps_needed += 1
            array_string[i + 2] = "1"
    return steps_needed


print(beautiful_binary_string('0101010'))
print(beautiful_binary_string('01100'))
