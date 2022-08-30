test_cases = int(input())

for t in range(test_cases):
    parts, maximum_holds = map(int, input().split())

    each_style_number = [int(i) for i in input().split()]
    each_style_number.sort()
    answer = "YES"

    if parts > maximum_holds * 2:
        answer = "NO"
    else:
        each_style_number_values = {}
        first_smallest = 0
        second_smallest = 0
        j = 0
        for k in each_style_number:
            if j % 2 == 0:
                first_smallest += k
            else:
                second_smallest += k
            j += 1
            each_style_number_values.setdefault(k, 0)
            each_style_number_values[k] += 1
            if each_style_number_values[k] > 2:
                answer = "NO"
                break

    print("Case #{}: {}".format(t + 1, answer))
