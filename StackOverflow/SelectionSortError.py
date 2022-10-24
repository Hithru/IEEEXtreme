def selectionsort(lst, target):
    first = 0
    last = len(lst) - 1
    for step in range(len(lst)-1):
        for i in range(step + 1, len(lst)):
            min_idx = i
            if lst[min_idx] < lst[step]:
                #swap the elements
                (lst[min_idx], lst[step]) = (lst[step], lst[min_idx])

    while (first <= last):
        mid = (first + last) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            first = mid + 1
        else:
            last = mid - 1
    return None

def verify(index):
    if index is not None:
        print("Target found at index", index)
    else:
        print("Target not found")

data = [200, 12, 3, 100, 2]
result = selectionsort(data, 100)
verify(result)
print("The sorted list is \n", data)