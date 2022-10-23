t = int(input().strip())
drain = []

outlets = 0
for i in range(t):
    n, m, d = map(int, input().strip().split())
    for j in range(d):
        level = []
        for i in range(m):
            row = input()
            level.append(row)
            for k in row:
                if k == "*":
                    outlets += 3
                elif k == "o":
                    outlets += 2

        none = input()
        drain.append(level)

print(drain, outlets)