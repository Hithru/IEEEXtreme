# Challenge Name: Manasa and Stones
# Difficulty: Easy

def stones(n, a, b):
    values = set()
    for i in range(n):
        values.add((n - 1 - i) * a + i * b)

    return sorted([i for i in values])


print(stones(3, 1, 2))
print(stones(4, 10, 100))
