# HackerRank
# IEEEXtreme Practice Community
# Xtreme 10.0 - Dog Walking
# Constraints 1 ≤ K ≤ N ≤ 10^5

test_cases = int(input())

for i in range(test_cases):
    n, k = map(int, input().split())

    dogs = []
    for j in range(n):
        dogs.append(int(input()))

    if n == k:
        print(0)
    else:
        dogs.sort()
        difference = []

        for l in range(1, len(dogs)):
            difference.append(dogs[l] - dogs[l - 1])
        difference.sort()

        print(sum(difference[:n - k]))


# Sample Input
#
# 2
# 4 2
# 3
# 5
# 1
# 1
# 5 4
# 30
# 40
# 20
# 41
# 50
