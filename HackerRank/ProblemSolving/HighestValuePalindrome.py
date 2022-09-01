# Challenge Name: Highest Value Palindrome
# Difficulty: Medium

def highest_value_palindrome(string: str, n: int, k: int):
    must_changes = []
    must_change_index = {}
    list_string = list(string)
    for i in range(n // 2):
        if string[i] != string[-(i + 1)]:
            max_element = max(int(string[i]), int(string[-(i + 1)]))

            must_change_index.setdefault(i, True)
            must_changes.append((i, string[i], string[-(i + 1)]))

    if len(must_changes) > k:
        return str("-1")

    changes_left = k - len(must_changes)
    print("changes left", changes_left)
    while changes_left > 1:
        for i in range(n // 2):
            if string[i] != "9":
                list_string[i] = "9"
                changes_left -= 1
                if string[-(i + 1)] != "9":
                    list_string[-(i + 1)] = "9"
                    changes_left -= 1

                if i in must_change_index:
                    del must_change_index[i]
                    must_changes.remove((i, string[i], string[-(i + 1)]))
                    changes_left += 1
            if changes_left <= 1:
                break
    for tup in must_changes:
        if changes_left >= 1:
            value = 9
            changes_left -= 1
        else:
            value = max(int(tup[1]), int(tup[2]))
        list_string[tup[0]] = str(value)
        list_string[-(tup[0] + 1)] = str(value)

    if changes_left >= 1:

        if n % 2 == 1:
            list_string[n // 2] = "9"
    print(list_string)
    return "".join(list_string)


print(highest_value_palindrome("3943", 4, 1))
print(highest_value_palindrome("092282", 6, 3))
