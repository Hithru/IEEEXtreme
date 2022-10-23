counts = [dict() for i in range(8)]

with open("input.txt", 'r', encoding='utf-8') as file:
    for li in file:

        line =li.strip()
        if len(line) > 10:
            pass
        else:
            for k in range(8):
                if k < len(line):
                    counts[k].setdefault(line[k], 0)
                    counts[k][line[k]] += 1
                else:
                    counts[k].setdefault(" ", 0)
                    counts[k][" "] += 1

    space_found = False
    start_count = 11
    for dicts in counts:
        line_values = []
        n = 0
        sorted_dict = sorted(dicts.items(), key=lambda e: e[1], reverse=True)

        for key, value in sorted_dict:

            if n == start_count:
                break
            else:
                line_values.append(key)
                n +=1

        print("".join(line_values).replace(" ",""))

