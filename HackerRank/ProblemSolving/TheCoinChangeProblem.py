# Challenge Name: The Coin Change Problem
# Difficulty: Medium

def get_ways(total, coins):
    ways_memory = {}

    def count_ways(index, amount):
        if amount == 0:
            return 1
        if amount < 0 or index == len(coins):
            return 0
        if (index, amount) in ways_memory:
            return ways_memory[(index, amount)]
        num_ways = 0
        coin = coins[index]

        for refactor in range(amount // coin + 1):
            payment = coin * refactor
            num_ways += count_ways(index + 1, amount - payment)
        ways_memory[(index, amount)] = num_ways
        return num_ways

    return count_ways(0, total)


print(get_ways(4, [1, 2, 3]))
print(get_ways(10, [2, 5, 3, 6]))
