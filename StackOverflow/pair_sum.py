def equal_pair(arr):
    sorted_array = sorted(arr)
    equal_pairs = []
    pair_sum = (2*sum(arr))/len(arr)
    for i in range(len(arr) // 2):
        if sorted_array[i] + sorted_array[-(i + 1)] == pair_sum:
            equal_pairs.append([sorted_array[i], sorted_array[-(i + 1)]])
        else:
            return "Equal Pairs not possible "

    return equal_pairs


print(equal_pair([1, 2, 3, 2]))
