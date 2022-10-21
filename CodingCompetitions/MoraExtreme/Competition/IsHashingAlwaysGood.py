import itertools

string = input()
values = [[] * len(string)]
ord_value_list = [ord(i) for i in string]


def hash_value(string):
    p = 1
    hash_value = 0
    for k in string:
        hash_value += p * ord(k)
        p *= 5
    return hash_value % 10 ** len(string)


values_dict = {}
answer = 0
used_p = {}
for p in itertools.permutations(string):
    if p in used_p:
        pass
    else:
        value = hash_value(p)
        if value in values_dict:
            answer += 1
        else:
            values_dict[value] = 1
        used_p[p] = True
print(answer)

# Sample Input 0
#
# asxz


# Sample Output 0
#
# 1
