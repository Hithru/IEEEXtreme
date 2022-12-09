t,n,g = map(int,input().strip().split())

for i in range(t):
    sequence = list(map(int,input().strip().split()))
    sequence_values = {}
    count_pairs = 0
    for num in sequence:
        sequence_values.setdefault(num,0)
        if sequence_values[num] == 2:
            print("NOT SAFE")
            break
        sequence_values[num] +=1
        if sequence_values[num] == 2:
            count_pairs +=1
    else:
        if count_pairs != g:
            print("NOT SAFE")
        else:
            print("SAFE")

# Sample Input 0
#
# 2 6 2
# 4 5 0 4 0 2
# 2 5 4 3 6 6
# Sample Output 0
#
# SAFE
# NOT SAFE