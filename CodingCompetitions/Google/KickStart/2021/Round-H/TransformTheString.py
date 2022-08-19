test_cases = int(input())

for t in range(test_cases):
    letters = list(input())
    values = list(input())
    cost = 0
    letters_min_value = {}
    for letter in letters:
        min_value = 26
        if letter in letters_min_value:
            cost += letters_min_value[letter]
            continue
        for val in values:
            right_value = ord(letter) - ord(val)
            left_value = ord(val) - ord(letter)

            if right_value < 0:
                right_value += 26
            if left_value < 0:
                left_value += 26
            value = min(right_value, left_value)
            if value < min_value:
                min_value = value
        letters_min_value[letter] = min_value
        cost += min_value

    print("Case #{}: {}".format(t + 1, cost))

# input
# 2
# abcd
# a
# pppp
# p
