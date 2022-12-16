n, x, y = map(int, input().strip().split())

keyboard_price = list(map(float, input().strip().split()))
mouse_price = list(map(float, input().strip().split()))

keyboard_price.sort()
mouse_price.sort(reverse=True)

key_start = 0
mouse_start = 0

maximum_amount = -1
for i in range(x):
    while mouse_start < y:
        price = keyboard_price[i] + mouse_price[mouse_start]
        if price <= float(n):
            if price >= maximum_amount:
                maximum_amount = price
            break
        else:
            mouse_start += 1
print(int(maximum_amount))

# Sample Input 0
#
# 10 2 3
# 3 1
# 5 2 8
# Sample Output 0
#
# 9