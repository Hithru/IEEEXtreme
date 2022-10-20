t = int(input())
for i in range(t):
    m = int(input())
    answer = ""
    for j in range(m):
        string = input()
        sort_word = "".join(sorted(string))
        answer += sort_word[0]
    print("".join(sorted(answer)))

# Sample Input 0

# 2
# 3
# asdfsdf
# sdfsdfb
# sfsdfd
# 2
# xyztxc
# pqurstwxe

# Sample Output 0

# abd
# ce
