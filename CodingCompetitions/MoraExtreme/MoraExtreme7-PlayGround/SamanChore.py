# Challenge Name: Saman Chore
# Difficulty: Easy

k, l = map(int, input().split())

must_completed = {}
for j in range(l):
    m, n = map(int, input().split())
    must_completed.setdefault(n, [])
    must_completed[n].append(m)

chore_list = [int(i) for i in input().split()]

completed_list = []
for chore in chore_list:
    if chore in must_completed:
        completed = must_completed[chore]
        check = all(item in completed_list for item in completed)
        if not check:
            print("NO")
            break
    completed_list.append(chore)
else:
    print("YES")

# Sample Input
# 520 8
# 111 115
# 111 110
# 210 111
# 210 110
# 210 223
# 223 203
# 223 450
# 450 520
# 111 115 110 210 223 203 450 520

# Sample Output
# NO
