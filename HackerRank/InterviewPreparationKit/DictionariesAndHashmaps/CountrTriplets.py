# Challenge Name: Count Triplets
# Difficulty: Medium

def countTriplets(arr, r):
    maximum = max(arr)
    highest = 1
    geometric = 1
    geometric_dic = {1: 0}
    while geometric < maximum:
        geometric *= r
        geometric_dic[geometric] = highest
        highest += 1

    elements = [0] * highest
    print(geometric_dic)
    i = 0
    while i < len(arr):
        if arr[i] == 1:
            elements[0] += 1
        elif arr[i] in geometric_dic:
            elements[geometric_dic[arr[i]]] += 1
        i += 1
    print(elements)
    answer = 0
    for j in range(len(elements) - 2):
        answer = answer + elements[j] * elements[j + 1] * elements[j + 2]
    print(answer)
    return answer


print(countTriplets([1, 3, 9, 9, 27, 81], 3))
