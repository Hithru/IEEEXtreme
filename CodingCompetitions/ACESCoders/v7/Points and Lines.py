n = int(input().strip())

coordinates = []
for i in range(n):
    x, y = map(float, input().strip().split())
    coordinates.append((x, y))

if n < 5:
    print("-1")
else:
    colinear = [(0, 1, 2), (0, 1, 3), (0, 1, 4), (0, 2, 3), (0, 2, 4), (0, 3, 4), (1, 2, 3), (1, 2, 4), (1, 3, 4),
                (2, 3, 4)]
    first_line = []
    second_line = []
    start = ()
    stop = False
    for cord in colinear:
        x1, y1 = coordinates[cord[0]][0], coordinates[cord[0]][1]
        x2, y2 = coordinates[cord[1]][0], coordinates[cord[1]][1]
        x3, y3 = coordinates[cord[2]][0], coordinates[cord[2]][1]
        start = cord
        if x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2) == 0:
            for l in range(0, 5):
                if l in cord:
                    first_line.append(str(l))
            break
    else:
        print("-1")
        stop = True

    if not stop:
        for m in range(0, len(coordinates)):
            if m in start:
                continue
            fx1, fy1 = coordinates[int(first_line[0])][0], coordinates[int(first_line[0])][1]
            fx2, fy2 = coordinates[int(first_line[1])][0], coordinates[int(first_line[1])][1]

            x3, y3 = coordinates[m][0], coordinates[m][1]

            if fx1 * (fy2 - y3) + fx2 * (y3 - fy1) + x3 * (fy1 - fy2) == 0:
                first_line.append(str(m))
                continue

            if len(second_line) < 2:
                second_line.append(str(m))
                continue

            sx1, sy1 = coordinates[int(second_line[0])][0], coordinates[int(second_line[0])][1]
            sx2, sy2 = coordinates[int(second_line[1])][0], coordinates[int(second_line[1])][1]
            if sx1 * (sy2 - y3) + sx2 * (y3 - sy1) + x3 * (sy1 - sy2) == 0:
                second_line.append(str(m))
            else:
                print('-1')
                break

        else:
            if len(second_line) < 2:
                print("-1")
            else:
                print(" ".join(first_line))
                print(" ".join(second_line))

# Sample Input 0
#
# 5
# 9 11
# 2 4
# 8 9
# 5 7
# 2 3
# Sample Output 0
#
# 0 1 3
# 2 4