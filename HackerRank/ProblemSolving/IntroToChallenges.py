# Challenge Name: Intro to Challenges
# Difficulty: Easy

def intro_tutorial(V, arr):
    return binary_search(arr, V, 0, len(arr))


def binary_search(arr, value, start, end):
    if end >= start:
        mid_index = (start + end) // 2
        if arr[mid_index] == value:
            return mid_index
        elif arr[mid_index] > value:
            return binary_search(arr, value, start, end - 1)
        else:
            return binary_search(arr, value, mid_index + 1, end)
    else:
        return None


print(intro_tutorial(4, [1, 4, 5, 7, 9, 12]))
