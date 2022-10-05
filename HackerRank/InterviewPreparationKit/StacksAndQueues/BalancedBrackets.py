# Challenge Name: Balanced Brackets
# Difficulty: Medium

def isBalanced(string_name: str):
    brackets = []
    close_bracket = {"(": ")", "[": "]", "{": "}"}
    for bracket in string_name:
        print(brackets)
        if bracket == "(" or bracket == "{" or bracket == "[":
            brackets.append(bracket)
        else:
            if len(brackets) == 0:
                return "NO"
            else:
                if bracket == close_bracket[brackets[-1]]:
                    element = brackets.pop()
                else:
                    return "NO"

    return "YES" if len(brackets) == 0 else "NO"


string = input()
print(isBalanced(string))
