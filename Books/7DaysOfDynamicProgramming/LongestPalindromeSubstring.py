# Book : 7 Days with Dynamic Programming
# Problem : Longest Palindrome Substring

# word1 : aabac
# Answer : aba
# word2 : gogogh
# Answer : gogog

def longest_palindrome_substring(string: str):
    n = len(string)
    # whether substring from index i to j is a palindrome or not
    palindrome_maximum_length = 0
    maximum_palindrome_indexes = (0, 0)
    substring_palindrome = {}
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            substring_palindrome.setdefault((i, j), False)
            if i == j:
                substring_palindrome[(i, j)] = True
            elif string[i] == string[j]:
                if j - i == 1:
                    substring_palindrome[(i, j)] = True
                else:
                    substring_palindrome.setdefault((i + 1, j - 1), False)
                    substring_palindrome[(i, j)] = substring_palindrome[(i + 1, j - 1)]

            if substring_palindrome[(i, j)] and j - i >= palindrome_maximum_length:
                palindrome_maximum_length = j - i
                maximum_palindrome_indexes = (i, j)

    return palindrome_maximum_length, maximum_palindrome_indexes, string[maximum_palindrome_indexes[0]:
                                                                         maximum_palindrome_indexes[1] + 1]


print(longest_palindrome_substring("aabac"))
print(longest_palindrome_substring("gogogh"))
