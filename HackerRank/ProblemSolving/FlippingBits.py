# Challenge Name: Flipping Bits
# Difficulty: Easy

def flipping_bits(n: int):
    bits = [0] * 32
    index = 0
    while n > 0:
        bits[index] = n % 2
        n = n // 2
        index += 1
    answer = 0
    power = 1
    for k in range(32):
        if bits[k] == 0:
            answer += power
        power *= 2
    return answer


print(flipping_bits(4))
