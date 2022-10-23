test_cases = int(input())

for test_case in range(test_cases):
    length = int(input())

    robot_path = []
    for i in range(length):
        path = input()
        robot_path.append(list(path))



    num_patterns = int(input())
    patterns = []
    for k in range(num_patterns):
        r,c = map(int,input().strip().split())
        patterns.append((r,c))

    tries = 0

    robot_position = (0,0)
    already_achieved_place_robot = {}
    robots_path = []
    while True:
        robots_path.append(robot_position)
        already_achieved_place_robot.setdefault(robot_position,0)
        already_achieved_place_robot[robot_position] +=1
        if already_achieved_place_robot[robot_position] == 2:
            break
        robot_next_symbol = robot_path[robot_position[0]][robot_position[1]]

        if robot_next_symbol == ">":
            robot_position = (robot_position[0],robot_position[1]+1)
        elif robot_next_symbol == "<":
            robot_position = (robot_position[0], robot_position[1] - 1)
        elif robot_next_symbol == "^":
            robot_position = (robot_position[0]-1, robot_position[1])
        elif robot_next_symbol == "v":
            robot_position = (robot_position[0]+1, robot_position[1])


    #
    # robot_position = (0,0)
    # already_achieved_place_robot = {}
    # while tries < 1000000:
    #     dust_pattern=patterns[tries%num_patterns]
    #
    #     if dust_pattern == robot_position:
    #         print(tries)
    #         break
    #     already_achieved_place_robot.setdefault(robot_position,0)
    #     already_achieved_place_robot[robot_position] +=1
    #     if already_achieved_place_robot[robot_position] == num_patterns:
    #
    #         print("never")
    #         break
    #     tries +=1
    #     robot_next_symbol = robot_path[robot_position[0]][robot_position[1]]
    #
    #     if robot_next_symbol == ">":
    #         robot_position = (robot_position[0],robot_position[1]+1)
    #     elif robot_next_symbol == "<":
    #         robot_position = (robot_position[0], robot_position[1] - 1)
    #     elif robot_next_symbol == "^":
    #         robot_position = (robot_position[0]-1, robot_position[1])
    #     elif robot_next_symbol == "v":
    #         robot_position = (robot_position[0]+1, robot_position[1])
    # else:
    #     print("never")