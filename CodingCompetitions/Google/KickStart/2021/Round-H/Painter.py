test_cases = int(input())

for t in range(test_cases):
    squares = int(input())
    colors = list(input())

    squares = []
    red_strokes = 0
    blue_strokes = 0
    yellow_stokes = 0

    red_strokes_happening = False
    blue_strokes_happening = False
    yellow_strokes_happening = False
    first_colored_square_found = False
    for i in range(len(colors)):
        color = colors[i]
        if color != "U":
            first_colored_square_found = True
        if not first_colored_square_found:
            continue
        if color == "R":
            if not red_strokes_happening:
                red_strokes_happening = True
            if blue_strokes_happening:
                blue_strokes_happening = False
                blue_strokes +=1
            if yellow_strokes_happening:
                yellow_strokes_happening = False
                yellow_stokes +=1
        elif color == "Y":
            if not yellow_strokes_happening:
                yellow_strokes_happening = True
            if blue_strokes_happening:
                blue_strokes_happening = False
                blue_strokes +=1
            if red_strokes_happening:
                red_strokes_happening = False
                red_strokes += 1
        elif color == "B":
            if not blue_strokes_happening:
                blue_strokes_happening = True
            if yellow_strokes_happening:
                yellow_strokes_happening = False
                yellow_stokes += 1
            if red_strokes_happening:
                red_strokes_happening = False
                red_strokes += 1
        elif color == "O":
            if not yellow_strokes_happening:
                yellow_strokes_happening = True
            if not red_strokes_happening:
                red_strokes_happening = True
            if blue_strokes_happening:
                blue_strokes_happening = False
                blue_strokes +=1
        elif color == "P":
            if not blue_strokes_happening:
                blue_strokes_happening = True
            if not red_strokes_happening:
                red_strokes_happening = True
            if yellow_strokes_happening:
                yellow_strokes_happening = False
                yellow_stokes += 1
        elif color == "G":
            if not yellow_strokes_happening:
                yellow_strokes_happening = True
            if not blue_strokes_happening:
                blue_strokes_happening = True
            if red_strokes_happening:
                red_strokes_happening = False
                red_strokes += 1
        elif color == "A":
            if not yellow_strokes_happening:
                yellow_strokes_happening = True
            if not red_strokes_happening:
                red_strokes_happening = True
            if not blue_strokes_happening:
                blue_strokes_happening = True
        elif color == "U":
            if red_strokes_happening:
                red_strokes_happening = False
                red_strokes += 1
            if blue_strokes_happening:
                blue_strokes_happening = False
                blue_strokes += 1
            if yellow_strokes_happening:
                yellow_strokes_happening = False
                yellow_stokes += 1

    if red_strokes_happening:
        red_strokes_happening = False
        red_strokes+=1
    if blue_strokes_happening:
        blue_strokes_happening = False
        blue_strokes +=1
    if yellow_strokes_happening:
        yellow_strokes_happening = False
        yellow_stokes +=1

    print("Case #{}: {}".format(t + 1, blue_strokes+red_strokes+yellow_stokes))