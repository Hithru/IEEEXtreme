# Pokemon Evolution
# Time limit: 2000 ms
# Memory limit: 128 MB


pokemon, candy, price_pokeman, sell_pokemon = map(int, input().split())

candy_man = candy // price_pokeman

candy = candy - price_pokeman * candy_man
pokemon = pokemon - candy_man

while True:
    if (pokemon == 0):
        break

    candy += sell_pokemon
    pokemon -= 1
    while True:
        if candy > price_pokeman and pokemon > 0:
            candy -= price_pokeman
            pokemon -= 1
            candy_man += 1
        else:
            break

print(candy_man)
