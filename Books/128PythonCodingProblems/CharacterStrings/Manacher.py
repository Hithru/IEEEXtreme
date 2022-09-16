def manacher(string):
    assert set.isdisjoint({'$', '^', '#'}, string)
    if string == '':
        return 0, 1
    transoformed_string = '^#' + "#".join(string) + "#$"
    c = 1
    d = 1
    p = [0] * len(transoformed_string)

    for i in range(2, len(transoformed_string) - 1):
        mirror = 2 * c - i
        p[i] = max(0, min(d - i, p[mirror]))
        while transoformed_string[i + 1 + p[i]] == transoformed_string[i - 1 - p[i]]:
            p[i] += 1
        if i + p[i] > d:
            c = i
            d = i + p[i]
    (k, i) = max((p[i], i) for i in range(1, len(transoformed_string) - 1))

    return (i - k) // 2, (i + k) // 2, string[(i - k) // 2: (i + k) // 2]


print(manacher("babcbabcbaccba"))
