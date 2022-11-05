def primes(n):
    prime_list = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if prime_list[i//2]:
            prime_list[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if prime_list[i]]

t = int(input())
test_cases = []
max_number = 1
high_list = []
low_list = []

for k in range(t):
    small,high = map(int,input().split())
    high_list.append(high)
    low_list.append(small)
    if high > max_number:
        max_number = high
    test_cases.append((small,high))
primes_list = primes(max_number+1)

low_list.sort()
high_list.sort(reverse=True)
high_dict = {}
low_dict = {}

current_index = 0
for k in low_list:
    while primes_list[current_index] < k and current_index < len(primes_list):
        current_index +=1
    low_dict[k] = primes_list[current_index]


current_index = len(primes_list) - 1
for h in high_list:
    while primes_list[current_index] > h and current_index >0:
        current_index -=1
    high_dict[h] = primes_list[current_index]


for tup in test_cases:
    if low_dict[tup[0]] < high_dict[tup[1]]:
        print(high_dict[tup[1]] - low_dict[tup[0]])
    else:
        print(0)