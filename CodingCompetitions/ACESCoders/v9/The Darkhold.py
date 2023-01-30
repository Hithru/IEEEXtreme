t = int(input())

for i in range(t):
    word = input()
    new_word = ""
    for k in word:
        if k in ["a", "e", "i", "o", "u"]:
            new_word += k

    sort_word = "".join(sorted(new_word))
    # print(new_word,sort_word)
    if new_word == sort_word:
        print("Easy")
    elif new_word[::-1] == sort_word:
        print("Medium")
    else:
        print("Hard")