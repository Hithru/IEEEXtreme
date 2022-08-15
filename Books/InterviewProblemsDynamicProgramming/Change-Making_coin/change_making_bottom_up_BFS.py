import collections


def simplest_change(coins, amount):
    solutions = {0: []}

    amounts_to_be_handled = collections.deque([0])

    while amounts_to_be_handled:
        paid = amounts_to_be_handled.popleft()
        solution = solutions[paid]

        if paid == amount:
            return solution

        for coin in coins:
            next_paid = paid + coin
            if next_paid > amount:
                continue
            if next_paid not in solutions:
                solutions[next_paid] = solution + [coin]
                amounts_to_be_handled.append(next_paid)

    return None


print(simplest_change([1, 2, 5], 12))
