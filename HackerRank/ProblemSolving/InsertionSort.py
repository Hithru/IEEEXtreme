# Challenge Name: Insertion Sort part 2
# Difficulty: Easy

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

        print(" ".join([str(k) for k in arr]))


print((insertion_sort([1, 4, 3, 5, 6, 2])))
