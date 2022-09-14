# Challenge Name: Jim And Orders
# Difficulty: Intermediate
from typing import List


def jim_and_orders(orders: List):
    customer_serve_time = [[i+1,orders[i][0] + orders[i][1]] for i in range(len(orders))]
    customer_serve_time.sort(key=lambda tup: tup[1])
    return [customer_serve_time[i][0] for i in range(len(customer_serve_time))]


print(jim_and_orders([[1, 3], [2, 3], [3, 3]]))