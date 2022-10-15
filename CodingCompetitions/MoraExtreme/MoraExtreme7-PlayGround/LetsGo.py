# Challenge Name: Let's Go
# Difficulty: Easy

n = int(input())

if n >= 2 and n <= 20:
    for i in range(n - 1):
        print("  " + "* " * (n - 1))

    for j in range(n + 1, -1, -1):
        print((n + 1 - j) * " " + j * "* ")

# Sample Input
# 4

# # Sample Output
#   * * *
#   * * *
#   * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
