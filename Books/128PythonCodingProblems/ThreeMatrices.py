from random import randint
from sys import stdin


def readint():
    return int(stdin.readline())


def readarray(typ):
    return list(map(typ, stdin.readline().split()))


def readmatrix(n):
    M = []
    for _ in range(n):
        row = readarray(int)
        assert len(row) == n
        M.append(row)
    return M


def mult(M, v):
    n = len(M)
    return [sum(M[i][j] * v[j] for j in range(n)) for i in range(n)]


def freivalds(A, B, C):
    n = len(A)
    x = [randint(0, 1000000) for j in range(n)]
    return mult(A, mult(B, x)) == mult(C, x)


if __name__ == "__main__":
    n = readint()
    new_list = readmatrix(n)
    length_of_dynamic_list = readmatrix(n)
    C = readmatrix(n)
    print(freivalds(new_list, length_of_dynamic_list, C))
