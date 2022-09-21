# Challenge Name: Frequencies Query
# Difficulty: Medium

def freqQuery(queries):
    values = {}
    frequency = {}
    answer = []
    for query in queries:
        operation = query[0]
        value = query[1]

        if operation == 1:
            if value in values:
                old_value = values[value]
                values[value] += 1
                if frequency[old_value] == 1:
                    del frequency[old_value]
                else:
                    frequency[old_value] -= 1
                frequency.setdefault(old_value + 1, 0)
                frequency[old_value + 1] += 1
            else:
                values[value] = 1
                frequency.setdefault(1, 0)
                frequency[1] += 1
        elif operation == 2:
            if value in values:
                old_value = values[value]
                if old_value == 1:
                    del values[value]
                else:
                    values[value] -= 1
                    frequency.setdefault(old_value - 1, 0)
                    frequency[old_value - 1] += 1

                if frequency[old_value] == 1:
                    del frequency[old_value]
                else:
                    frequency[old_value] -= 1
        else:
            if value in frequency:
                answer.append(1)
            else:
                answer.append(0)

    return answer


print(freqQuery([[1, 5], [1, 6], [3, 2], [1, 10], [1, 10], [1, 6], [2, 5], [3, 2]]))
