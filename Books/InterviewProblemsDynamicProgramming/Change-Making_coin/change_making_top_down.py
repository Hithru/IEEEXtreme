from functools import lru_cache


def make_change(coins, amount):
    @lru_cache(maxsize=None)
    def helper(helper_amount):
        # Handle payment of amount zero.
        if not helper_amount:
            return []
        # Negative amounts cannot be paid.
        if helper_amount < 0:
            return None

        optimal_result = None

        for coin in coins:
            partial_result = helper(helper_amount - coin)
            if partial_result is None:
                continue
            candidate = partial_result + [coin]

            if optimal_result is None or len(candidate) < len(optimal_result):
                optimal_result = candidate

        return optimal_result

    return helper(amount)


print(make_change([1, 2, 5], 10))
