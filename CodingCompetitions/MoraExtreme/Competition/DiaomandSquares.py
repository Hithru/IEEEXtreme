test_cases = int(input().strip())

for t in range(test_cases):
    n = int(input().strip())
    if n == 1:
        print("YES")
    else:
        coloumn_ones = {}
        rows = []
        for l in range(n):
            coloumn_ones.setdefault(l, 0)
            row_new = input().strip().split()
            rows.append(row_new)

        ones_row = 0
        twos_row = 0
        breaked_row = 0
        for j in range(n):
            col = 0
            new_value = 0
            row = rows[j]
            for i in row:
                if i == "1":
                    new_value += 1
                    coloumn_ones[col] += 1
                col += 1

            if new_value == 1:
                ones_row += 1
            elif new_value == 2:
                twos_row += 1
            else:
                print("NO")
                breaked_row = 1
                break

        if breaked_row == 0:
            if ones_row == 2:
                ones_colom = 0
                twos_colom = 0
                breaked_colom = 0
                for key, value in coloumn_ones.items():

                    if value > 2 or value == 0:
                        print("NO")
                        breaked_colom = 1
                        break
                    elif value == 2:
                        twos_colom += 1
                    else:
                        ones_colom += 1
                if breaked_colom == 0:
                    if ones_colom == 2:
                        print("YES")
                    else:
                        print("NO")
            else:
                print("NO")

# Sample Input

# 2
# 5
# 1 0 0 1 0
# 0 0 1 0 0
# 0 1 0 0 1
# 1 0 0 1 0
# 0 0 1 0 0
# 3
# 1 1 1
# 0 0 0
# 0 1 0


# Sample Output

# YES
# NO