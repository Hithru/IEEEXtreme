# Challenge Name: Extractor
# Difficulty: Easy

input_string = input()


def longest_palindrome_subsequence(string: str):
    n = len(string)
    subsequence_palindrome = {}
    for i in range(n):
        subsequence_palindrome.setdefault((i, i), 1)
    # whether substring from index i to j is a palindrome or not

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            subsequence_palindrome.setdefault((i, i), 0)
            subsequence_palindrome.setdefault((i + 1, j), 0)
            subsequence_palindrome.setdefault((i, j - 1), 0)
            subsequence_palindrome.setdefault((i + 1, j - 1), 0)
            if string[i] == string[j] and j - i + 1 == 2:
                subsequence_palindrome[(i, j)] = 2
            elif string[i] == string[j]:
                subsequence_palindrome[(i, j)] = subsequence_palindrome[(i + 1, j - 1)] + 2
            else:
                subsequence_palindrome[(i, j)] = max(subsequence_palindrome[(i, j - 1)],
                                                     subsequence_palindrome[(i + 1, j)])

    return subsequence_palindrome[(0, n - 1)]


print(longest_palindrome_subsequence(input_string))
