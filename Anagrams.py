# Challenge Name: Anagrams
# Time limit: 2000 ms
# Memory limit: 128 MB
# Contest: Beta Round 4
# Difficulty: Medium

num_words = int(input())
words_dic = {}
maximum = 1
for k in range(num_words):

    new = input()
    sort_word = ("").join(sorted(new))
    if sort_word not in words_dic:
        words_dic[sort_word] = 1
    else:
        words_dic[sort_word] += 1
        if maximum < words_dic[sort_word]:
            maximum = words_dic[sort_word]

print(maximum)

