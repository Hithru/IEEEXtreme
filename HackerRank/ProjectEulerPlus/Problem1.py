def s(number):
    return number * (number + 1) // 2


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip()) - 1
    print(s(n // 3) * 3 + s(n // 5) * 5 - s(n // 15) * 15)
