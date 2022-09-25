# Challenge Name: 3-divisible Pairs
# Time limit: 2000 ms
# Memory limit: 128 MB


N = input()
numbers = [int(i) for i in input().split(" ")]

answer = 0
difference_one = 0
difference_zero = 0
difference_two = 0
for number in numbers:
    if number % 3 == 1:
        difference_one += 1
    elif number % 3 == 2:
        difference_two += 1
    else:
        difference_zero += 1


answer = difference_one * difference_two + difference_zero * (difference_zero - 1) // 2

print(answer)
