amount = int(input())


def way(amount):
    max_five_thousands = amount // 5000
    max_thousands = amount // 1000
    max_five_hundred = amount // 500
    max_hundred = amount // 100

    for ft in range(max_five_thousands, -1, -1):

        for t in range(max_thousands, -1, -1):
            if t == 0 and ft > 0:
                continue
            for fh in range(max_five_hundred, -1, -1):
                if fh == 0 and t > 0:
                    continue
                h = (amount - (ft * 5000 + t * 1000 + fh * 500)) // 100
                if h <= 0:
                    continue
                if ft * 5000 + t * 1000 + fh * 500 + h * 100 == amount:
                    print(h, fh, t, ft)
                    return


way(amount)