phrases_to_encrypt = int(input())
num_xml_representations = int(input())

rows, column = map(int, input().strip().split(","))

cipher_type = input()

texts_to_cipher = []
for i in range(phrases_to_encrypt):
    phrase = input().strip()
    texts_to_cipher.append(phrase)

cipher_grid = []
c = 0
r = 0
row  = []
encrypt_dict = {}
for j in range(num_xml_representations):
    xml_repres = input()

    tag_open = False
    if c < rows:
        for k in xml_repres:
            if not tag_open:
                if k == "<":
                    tag_open = True
                else:

                    row.append(k)
                    if k not in encrypt_dict:
                        encrypt_dict[k] = (c+1,r+1)
                    else:
                        if cipher_type == "S":
                            if (c+1,r+1) < encrypt_dict[k]:
                                encrypt_dict[k] = (c+1,r+1)
                        else:
                            if (c+1,r+1) > encrypt_dict[k]:
                                encrypt_dict[k] = (c+1,r+1)
                    r +=1
                    if r == column:
                        r = 0
                        c += 1
                        cipher_grid.append(row)
                        row = []
            else:
                if k == ">":
                    tag_open = False
            if c == rows:
                break
for text in texts_to_cipher:
    answer = []
    for t in text:
        answer.append(str(encrypt_dict[t][0]))
        answer.append(str(encrypt_dict[t][1]))
    print(",".join(answer))
# print(cipher_grid)
# print(encrypt_dict)
