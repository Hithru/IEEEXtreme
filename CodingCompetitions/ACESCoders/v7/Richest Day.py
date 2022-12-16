n = int(input())

table = {}
answer = 0
intervals = []
for i in range(n):
    pay, start, end = map(int, input().strip().split())
    intervals.append((start, "a", pay))
    intervals.append((end, "e", pay))

final_answer = 0
current_pay = 0

intervals.sort()

for period in intervals:
    if period[1] == "a":
        current_pay += period[2]
        if current_pay > final_answer:
            final_answer = current_pay
    else:
        current_pay -= period[2]

print(final_answer)


# Sample Input 0
#
# 5
# 100 7 10
# 100 1 2
# 100 5 8
# 100 1 4
# 100 1 3
# Sample Output 0
#
# 300