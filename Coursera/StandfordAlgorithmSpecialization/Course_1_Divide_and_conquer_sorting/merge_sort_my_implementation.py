from typing import List


def merge(array: List[int], start: int, middle: int, end: int):
    left_length = middle - start+1
    right_length = end - middle
    left_part = [array[start + i] for i in range(left_length)]
    right_part = [array[middle + j+1] for j in range(right_length)]
    left_part.append(float('inf'))
    right_part.append(float('inf'))
    i = 0
    j = 0
    for k in range(start, end+1):
        if left_part[i] < right_part[j]:
            array[k] = left_part[i]
            i += 1
        else:
            array[k] = right_part[j]
            j += 1


def merge_sort(array: List[int], start: int, end: int):
    if start < end:
        middle = (start + end) // 2
        merge_sort(array, start, middle)
        merge_sort(array, middle + 1, end)
        merge(array, start, middle, end)


unsorted_array = [5, 3, 25, 10, 6, 20, 7, 8]
print(unsorted_array)
merge_sort(unsorted_array, 0, len(unsorted_array)-1)
print(unsorted_array)
