T = int(input())

for t in range(T):
    N = int(input())
    number = input()

    result = 1
    mul = 1
    prev_mul = 1
    prev_cin = number[0]
    # print(number)
    for i in range(1, len(number)):
        # print(i, end="")
        if (int(number[i - 1:i + 1]) <= N):
            temp = mul
            mul += prev_mul
            prev_mul = temp
        else:
            result *= mul
            mul = 1
            prev_mul = 1
        # print(result, end = ' ')
    # print()
    result *= mul
    print(result)