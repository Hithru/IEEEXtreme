import sys
sys.setrecursionlimit(10000000)
new_list = []
dynamic_list = [None for _ in range(1501)]
for i in range(1501):
    dynamic_list[i] = [None for _ in range(1201)]
    for j in range(1201):
        dynamic_list[i][j] = [-1, -1]

length_of_dynamic_list = len(dynamic_list)


def dynamically_solve(right_index, left_index, b):
    global dynamic_list, length_of_dynamic_list
    if dynamic_list[left_index][right_index][b] != -1:
        return dynamic_list[left_index][right_index][b]

    if left_index == length_of_dynamic_list:
        return 0

    if right_index == 0:
        return 0

    if b == 1:
        resolve = max(-new_list[left_index] + dynamically_solve(right_index, left_index + 1, 0), dynamically_solve(right_index, left_index + 1, 1))

    else:
        resolve = max(new_list[left_index] + dynamically_solve(right_index - 1, left_index + 1, 1), dynamically_solve(right_index, left_index + 1, 0))

    dynamic_list[left_index][right_index][b] = resolve
    return resolve


def best_final_profit(transaction_limit, hourly_prices):
    global dynamic_list, length_of_dynamic_list, new_list
    N = len(hourly_prices)
    new_list = [0 for _ in range(N)]
    new_list = hourly_prices.copy()

    for i in range(N + 1):
        for j in range(transaction_limit + 1):
            dynamic_list[i][j][1] = -1
            dynamic_list[i][j][0] = -1

    length_of_dynamic_list = N
    return dynamically_solve(transaction_limit, 0, 1)

transaction_limit = int(input())
hourly_prices = [int(i) for i in input().strip().split(",")]

print(best_final_profit(transaction_limit, hourly_prices))