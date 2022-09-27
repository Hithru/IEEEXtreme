# One Letter
# Time limit: 2000 ms
# Memory limit: 128 MB
# Contest: Beta Round 7
# Difficulty: Easy

n = int(input())
string = ""
for i in range(n):
    word = input()
    sorted_string = "".join(sorted(word))
    string += sorted_string[0]

answer = "".join(sorted(string))
print(answer)
