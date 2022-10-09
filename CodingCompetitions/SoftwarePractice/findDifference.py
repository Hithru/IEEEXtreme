def findDifferenceValue(firstString, secondString):
    print("first string :- ", firstString, len(firstString))
    print("second string :- ", secondString, len(secondString))
    if set(firstString) == set(secondString) and len(set(firstString)) == 1:
        return abs(len(firstString) - len(secondString))
    first_string_length = len(firstString)
    second_string_length = len(secondString)
    i = 0
    j = 0
    final_i_useds = [(-1, 0)]
    while i < first_string_length:
        if firstString[i] == secondString[j]:
            print(firstString[i], i, j)
            final_i_used = i

            i += 1
            j += 1
            final_i_useds.append((final_i_used, j))
        else:
            i += 1

        if j == len(secondString):
            return 0

    maximum_index = len(secondString) - 1
    print(final_i_useds, final_i_useds[-1][1], maximum_index)
    k = first_string_length - 1
    l = second_string_length - 1

    min_answer = len(secondString)
    for t in range(len(final_i_useds) - 1, -1, -1):
        while k > final_i_useds[t][0]:
            if secondString[l] == firstString[k]:
                print(secondString[l], k, l)
                k -= 1
                l -= 1
                maximum_index -= 1
            else:
                k -= 1
            if l == final_i_useds[t][1]:
                return 1

        answer = maximum_index - final_i_useds[t][1] + 1
        if answer < min_answer:
            min_answer = answer
    return min_answer


print(findDifferenceValue(
    "AILXFTYPSKFAASQOHHSQMHRGRUASWGSFFAXUHLFKBFWSLKYWSZOPJIECKTEXHNVPLUKILNBQIRRMYDNXJLBZAYEETRENKRECDZSF",
    "BLKMZJMMIBJJZSXNDIPNMQEEDAZORSEEANGLAUUFIISRKAZVHYNIRONDIAQHFPQUQRWZSCLJGRZLFNRXTANDQWBVEUXMOUHGXLMR"))
