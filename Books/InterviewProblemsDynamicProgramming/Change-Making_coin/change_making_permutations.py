from functools import lru_cache


def count_ways_to_pay(coins, amount):
    @lru_cache(maxsize=None)
    def count_ways_helper(helper_amount):
        if helper_amount == 0:
            return 1
        if helper_amount < 0:
            return 0
        num_ways = 0
        for first in coins:
            num_ways += count_ways_helper(helper_amount - first)
        return num_ways

    return count_ways_helper(amount)


print(count_ways_to_pay([1, 2, 5], 3))
