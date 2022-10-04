# Challenge Name: Recursive Digit Sum
# Difficulty: Medium

def superDigit(n, k):
    if len(str(n)) == 1:
        return n
    else:

        answer = 0
        for char in str(n):
            answer += int(char)
        return superDigit(answer * k, 1)


n = int(input())
k = int(input())
print(superDigit(n, k))
