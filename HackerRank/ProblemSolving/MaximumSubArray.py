# Challenge Name: The Maximum Subarray
# Difficulty: Medium

def max_subarray(arr):

    maximum_subarray_sum = -float('inf')
    maximum_negative_value = -float('inf')

    sum_of_positive_values = 0
    no_positive_value = True

    continues_subarray_sum = 0
    minimum_subarray_sum = 0

    for i in range(len(arr)):
        if arr[i] >= 0:
            no_positive_value = False
            sum_of_positive_values += arr[i]
        if arr[i] > maximum_negative_value:
            maximum_negative_value = arr[i]

        continues_subarray_sum += arr[i]
        if continues_subarray_sum < minimum_subarray_sum:
            minimum_subarray_sum = continues_subarray_sum

        current_highest_subarray_sum = continues_subarray_sum - minimum_subarray_sum

        if current_highest_subarray_sum > maximum_subarray_sum:
            maximum_subarray_sum = current_highest_subarray_sum

    if no_positive_value:
        return [maximum_negative_value, maximum_negative_value]
    else:
        return [maximum_subarray_sum, sum_of_positive_values]


print(max_subarray([2, -1, 2, 3, 4, -5]))
