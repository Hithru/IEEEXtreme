def maximum_border_length(word):
    n = len(word)
    window = [0] * n
    k = 0
    for i in range(1, n):
        while word[k] != word[i] and k > 0:
            k = window[k - 1]

        if word[k] == word[i]:
            k += 1

        window[i] = k

    return window


print(maximum_border_length("abaababaa"))
