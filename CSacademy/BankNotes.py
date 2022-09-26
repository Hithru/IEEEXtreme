# Challenge Name: BankNotes
# Time limit: 2000 ms
# Memory limit: 128 MB
# Difficulty: Easy

def banknotes(a, b, s, n):
    x = (s - b * n) // (a - b)
    return x if 0 <= x <= n else -1


a, b, s, n = map(int, input().split(' '))
answer = banknotes(a, b, s, n)
print(answer)
