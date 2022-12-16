start, end, modulo = map(int, input().strip().split())
answer = 0

difference = end - start + 1
k = 0
found_middle = False
for i in range(start, end + 1):
    ways = (end + 1 - i) * (i - start + 1)
    answer += ways * i

print(answer % modulo)

# Sample Input 0
#
# 3 5 101
# Sample Output 0
#
# 40