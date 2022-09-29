# Challenge Name: Shoe Pairs
# Time limit: 2000 ms
# Memory limit: 128 MB
# Contest: Round #38
# Difficulty: Easy

cases = int(input())
shoes = {}
answer = 0
for k in range(cases):
    size, direction = input().strip().split(" ")
    shoes.setdefault(size, [0, 0])
    if direction == "L":
        if shoes[size][1] > 0:
            answer += 1
            shoes[size][1] -= 1
        else:
            shoes[size][0] += 1
    else:
        if shoes[size][0] > 0:
            answer += 1
            shoes[size][0] -= 1
        else:
            shoes[size][1] += 1

print(answer)
