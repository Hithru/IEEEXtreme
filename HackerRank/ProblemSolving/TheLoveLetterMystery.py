# Challenge Name: The Love-Letter Mystery
# Difficulty: Easy


def love_letter_mystery(string: str) -> int:
    answer = 0
    for i in range(len(string) // 2):
        answer += (abs(ord(string[i]) - ord(string[-(i + 1)])))
    return answer


print(love_letter_mystery("abc"))
print(love_letter_mystery("abcba"))
print(love_letter_mystery("abcd"))
