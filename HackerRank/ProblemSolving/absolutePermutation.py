# Challenge Name: Absolute Permutation
# Difficulty: Intermediate

def absolute_permutation(n: int, k: int):
    if k == 0:
        return [i + 1 for i in range(n)]
    if n % (2 * k) != 0:
        return [-1]
    else:
        return [(i + 1) + (1 if (i // k) % 2 == 0 else -1) * k for i in range(n)]


print(absolute_permutation(100, 2))
print(absolute_permutation(10, 5))
print(absolute_permutation(7, 5))
