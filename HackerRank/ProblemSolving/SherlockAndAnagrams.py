# Challenge Name: Sherlock And Anagrams
# Difficulty: Easy
import math


def binomial_coefficient(n: int, k: int) -> int:
    n_fac = math.factorial(n)
    k_fac = math.factorial(k)
    n_minus_k_fac = math.factorial(n - k)
    return n_fac / (k_fac * n_minus_k_fac)


def sherlock_anagrams(s: str):
    sub_strings = {}
    for i in range(1, len(s) + 1):
        start_index = 0
        end_index = start_index + i
        while end_index <= len(s):
            string_portion = s[start_index:end_index]
            sorted_portion = "".join(sorted(string_portion))
            sub_strings.setdefault(sorted_portion, 0)
            sub_strings[sorted_portion] += 1
            start_index += 1
            end_index += 1
    answer = 0
    print(sub_strings)
    for k, v in sub_strings.items():
        if v > 1:
            answer += binomial_coefficient(v, 2)

    return int(answer)


print(sherlock_anagrams("abba"))
