from functools import lru_cache


def count_ways_to_pay(coins, amount):
    @lru_cache(maxsize=None)
    def count_ways_helper(index, helper_amount):
        if helper_amount == 0:
            return 1
        if helper_amount < 0 or index == len(coins):
            return 0
        num_ways = 0
        coin = coins[index]

        for repeats in range(helper_amount // coin + 1):
            payment = coin * repeats
            num_ways += count_ways_helper(index + 1, helper_amount - payment)
        return num_ways

    return count_ways_helper(0, amount)


print(count_ways_to_pay([1, 2, 5], 2))
