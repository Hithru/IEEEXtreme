s1 = int(input())
first_string = input()

s2 = int(input())
second_string = input()
word_dict = {}
pairs = 0

for s in first_string:
    word_dict.setdefault(s, 0)
    word_dict[s] += 1

for t in second_string:
    if t in word_dict:
        pairs += 1
        word_dict[t] -= 1
        if word_dict[t] == 0:
            del word_dict[t]

print(pairs)