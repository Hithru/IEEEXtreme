test_cases = int(input())

for t in range(test_cases):
    cells = int(input())
    bots = 0
    bots_turn = True
    index = 0
    while index < cells:
        if bots_turn:
            bots += 1
            index += 1
            bots_turn = False
        else:
            index += 4
            bots_turn = True

    print("Case #{}: {}".format(t + 1, bots))