# Challenge Name: Closet_number
# Difficulty: Easy

def closet_number(arr):
    arr.sort()
    min_difference = float('inf')
    difference = {}
    for i in range(len(arr) - 1):
        new_difference = arr[i + 1] - arr[i]
        difference.setdefault(new_difference, [])
        difference[new_difference].append(arr[i])
        difference[new_difference].append(arr[i + 1])
        if new_difference < min_difference:
            min_difference = new_difference

    return sorted(difference[min_difference])


print(closet_number([989, 191, 111]))