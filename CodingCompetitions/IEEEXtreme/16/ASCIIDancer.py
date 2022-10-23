t = int(input().strip())
commands = int(input().strip())

man1 = [" ", "o", " "]
man2 = ["/", "|", "\\"]
man3 = ["/", " ", "\\"]
turn = 0
invert_char = {">":"<","<":">","(":")",")":"(","/":"\\","\\":"/"," ":" "}
for i in range(commands):
    command = input()
    if command[:3] == "say":
        print(command[4:])
    else:
        if "left hand to head" in command:
            man1[2] = ")"
            man2[2] = " "
        elif "left hand to hip" in command:
            man1[2] = " "
            man2[2] = ">"
        elif "left hand to start" in command:
            man1[2] = " "
            man2[2] = "\\"
        elif "left leg in" in command:
            man3[2] = ">"
        elif "left leg out" in command:
            man3[2] = "\\"
        elif "right hand to head" in command:
            man1[0] = "("
            man2[0] = " "
        elif "right hand to hip" in command:
            man1[0] = " "
            man2[0] = "<"
        elif "right hand to start" in command:
            man1[0] = " "
            man2[0] = "/"
        elif "right leg in" in command:
            man3[0] = "<"
        elif "right leg out" in command:
            man3[0] = "/"
        elif "turn" in command:
            turn = turn + 1

        if turn %2 == 0:
            print("".join(man1))
            print("".join(man2))
            print("".join(man3))
        else:
            invert_man1 = [invert_char[man1[2]],man1[1],invert_char[man1[0]]]
            invert_man2 = [invert_char[man2[2]], man2[1], invert_char[man2[0]]]
            invert_man3 = [invert_char[man3[2]], man3[1], invert_char[man3[0]]]

            print("".join(invert_man1))
            print("".join(invert_man2))
            print("".join(invert_man3))