# Challenge Name: Find Median
# Difficulty: Easy

def find_median(arr):
    arr.sort()
    return arr[len(arr) // 2]
