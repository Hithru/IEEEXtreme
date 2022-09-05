# Challenge Name: Separate Numbers
# Difficulty: Easy

def separate_numbers(s: str):
    i = 1
    while i < len(s) // 2 + 1:
        string_portion = s[:i]
        next_string = str(int(string_portion) + 1)
        if next_string == s[i:i + len(next_string)]:
            build_string = s[:i]
            k = 1
            while len(build_string) < len(s):
                next_string = str(int(string_portion) + k)
                build_string = build_string + next_string
                k += 1

            if build_string == s:
                answer = "YES " + string_portion
                return answer

        i += 1
    return "NO"


print(separate_numbers('91011'))
print(separate_numbers('010203'))
print(separate_numbers('1234'))
print(separate_numbers('99100'))
