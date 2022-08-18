# Challenge Name: The Power Sum
# Difficulty: Intermediate

def power_sum(number: int, power: int):
    subsets = []
    answer = 0
    for i in range(1, number + 2):
        if i ** power > number:
            break
        elif i ** power == number:
            answer += 1
            break
        for j in range(len(subsets)):
            new_set = subsets[j] + [i ** power]
            sum_new_set = sum(new_set)
            if sum_new_set == number:
                answer += 1
            elif sum_new_set < number:
                subsets.append(new_set)
        subsets.append([i ** power])
    print(subsets)
    return answer


print(power_sum(10, 2))
print(power_sum(100, 2))
print(power_sum(100, 3))
