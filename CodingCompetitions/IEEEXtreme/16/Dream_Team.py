# a simple parser for python. use get_number() and get_word() to read
budget = int(input())

number_pg = int(input())
pg_dict = {}

for i in range(number_pg):
    name, value = input().strip().split()
    value = int(value)
    if value in pg_dict:
        if name < pg_dict[value]:
            pg_dict[value] = name
    else:
        pg_dict[value] = name

number_sg = int(input())
sg_dict = {}

for i in range(number_sg):
    name, value = input().strip().split()
    value = int(value)
    if value in sg_dict:
        if name < sg_dict[value]:
            sg_dict[value] = name
    else:
        sg_dict[value] = name

number_sf = int(input())
sf_dict = {}

for i in range(number_sf):
    name, value = input().strip().split()
    value = int(value)
    if value in sf_dict:
        if name < sf_dict[value]:
            sf_dict[value] = name
    else:
        sf_dict[value] = name

number_pf = int(input())
pf_dict = {}

for i in range(number_pf):
    name, value = input().strip().split()
    value = int(value)
    if value in pf_dict:
        if name < pf_dict[value]:
            pf_dict[value] = name
    else:
        pf_dict[value] = name

number_c = int(input())
c_dict = {}

for i in range(number_c):
    name, value = input().strip().split()
    value = int(value)
    if value in c_dict:
        if name < c_dict[value]:
            c_dict[value] = name
    else:
        c_dict[value] = name



pg_values = sorted(pg_dict.keys(), reverse=True)
sg_values = sorted(sg_dict.keys(), reverse=True)
sf_values = sorted(sf_dict.keys(), reverse=True)
pf_values = sorted(pf_dict.keys(), reverse=True)
c_values = sorted(c_dict.keys(), reverse=True)



c_pf_value_used = {}
c_pf_sf_value_used = {}
c_pf_sf_sg_value_used = {}
max_value = 0
answer = []
for c in c_values:
    if c > budget:
        continue
    for pf in pf_values:
        if c + pf > budget or c + pf in c_pf_value_used:
            continue
        c_pf_value_used.setdefault(c + pf, True)
        for sf in sf_values:
            if c + pf + sf > budget or c + pf + sf in c_pf_sf_value_used:
                continue
            c_pf_sf_value_used.setdefault(c + pf + sf, True)
            for sg in sg_values:
                if c + pf + sf + sg > budget or c + pf + sf + sg in c_pf_sf_sg_value_used:
                    continue
                c_pf_sf_sg_value_used.setdefault(c + pf + sf + sg, True)
                for pg in pg_values:
                    if c + pf + sf + sg + pg > budget:
                        continue
                    else:
                        if c + pf + sf + sg + pg > max_value:
                            max_value = c + pf + sf + sg + pg
                            answer = [pg_dict[pg], sg_dict[sg], sf_dict[sf], pf_dict[pf], c_dict[c]]
                            break
print("\n".join(answer))
