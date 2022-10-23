test_cases = int(input())

for test_case in range(test_cases):
    rows, columns = map(int, input().strip().split())
    maze = []
    pacman_start = (-1,-1)
    ghost_start = (-1,-1)
    for k in range(rows):
        r = input()
        row = []
        for i in range(len(r)):
            row.append(r[i])
            if r[i] == "P":
                pacman_start = (k,i)
            if r[i] == "G":
                ghost_start = (k,i)
        maze.append(row)
    if ghost_start == (-1,-1):
        print("INFINITE STAY")
    else:

        t = 0
        pacman_nodes = [(pacman_start[0],pacman_start[1],"")]
        ghost_nodes = [(ghost_start[0],ghost_start[1])]
        ghost_nodes_dict = {(ghost_start[0],ghost_start[1]):True}
        answer = ""
        answer_strings = []
        lowest_place_achieved = (pacman_start[0],pacman_start[1])
        lowest_place_achieved_path = ""
        while t < 15 and len(pacman_nodes) > 0:
            pacman_next_nodes = set()
            pacman_nodes_without_paths = set()
            path_dict = {}
            for p_node in pacman_nodes:

                #down
                if p_node[0]+1 < rows and maze[p_node[0] + 1][p_node[1]] != "X" and (len(p_node[2]) == 0 or p_node[2][-1] != "U") and (p_node[0] + 1, p_node[1]) not in ghost_nodes_dict:
                    pacman_next_nodes.add((p_node[0] + 1,p_node[1],p_node[2]+"D"))
                    pacman_nodes_without_paths.add((p_node[0] + 1, p_node[1]))
                    path_dict[(p_node[0] + 1, p_node[1])] = p_node[2]+"D"
                    if (p_node[0] + 1, p_node[1]) < lowest_place_achieved:
                        lowest_place_achieved = (p_node[0] + 1, p_node[1])
                        lowest_place_achieved_path = p_node[2]+"D"
                    elif (p_node[0] + 1, p_node[1]) == lowest_place_achieved:
                        if p_node[2]+"D" < lowest_place_achieved_path:
                            lowest_place_achieved_path = p_node[2]+"D"
                #up
                if p_node[0]-1 >= 0 and maze[p_node[0] - 1][p_node[1]] != "X" and (len(p_node[2]) == 0 or p_node[2][-1] != "D") and (p_node[0] - 1, p_node[1]) not in ghost_nodes_dict:
                    pacman_next_nodes.add((p_node[0] - 1,p_node[1],p_node[2]+"U"))
                    pacman_nodes_without_paths.add((p_node[0] - 1,p_node[1]))
                    path_dict[(p_node[0] -1 , p_node[1])] = p_node[2] + "U"

                    if (p_node[0] -1 , p_node[1]) < lowest_place_achieved:
                        lowest_place_achieved = (p_node[0] -1 , p_node[1])
                        lowest_place_achieved_path = p_node[2] + "U"
                    elif (p_node[0] -1 , p_node[1]) == lowest_place_achieved:
                        if p_node[2] + "U" < lowest_place_achieved_path:
                            lowest_place_achieved_path = p_node[2] + "U"
                #right
                if p_node[1]+1 < columns and maze[p_node[0]][p_node[1]+1] != "X" and (len(p_node[2]) == 0 or p_node[2][-1] != "L") and (p_node[0] , p_node[1]+1) not in ghost_nodes_dict:
                    pacman_next_nodes.add((p_node[0] ,p_node[1]+1,p_node[2]+"R"))
                    pacman_nodes_without_paths.add((p_node[0] ,p_node[1]+1))
                    path_dict[(p_node[0] , p_node[1]+1)] = p_node[2] + "R"

                    if (p_node[0] , p_node[1]+1) < lowest_place_achieved:
                        lowest_place_achieved = (p_node[0] , p_node[1]+1)
                        lowest_place_achieved_path = p_node[2] + "R"
                    elif (p_node[0] , p_node[1]+1) == lowest_place_achieved:
                        if p_node[2] + "R" < lowest_place_achieved_path:
                            lowest_place_achieved_path = p_node[2] + "R"
                #up
                if p_node[1] - 1 >= 0 and maze[p_node[0] ][p_node[1]-1] != "X" and (len(p_node[2]) == 0 or p_node[2][-1] != "R")and (p_node[0] , p_node[1] -1) not in ghost_nodes_dict:
                    pacman_next_nodes.add((p_node[0],p_node[1]-1,p_node[2]+"L"))
                    pacman_nodes_without_paths.add((p_node[0],p_node[1]-1))
                    path_dict[(p_node[0] , p_node[1]-1)] = p_node[2] + "L"

                    if (p_node[0] , p_node[1]-1) < lowest_place_achieved:
                        lowest_place_achieved = (p_node[0] , p_node[1]-1)
                        lowest_place_achieved_path = p_node[2] + "L"
                    elif (p_node[0] , p_node[1]-1) == lowest_place_achieved:
                        if p_node[2] + "L" < lowest_place_achieved_path:
                            lowest_place_achieved_path = p_node[2] + "L"
                #stay
                if (p_node[0] , p_node[1] -1) not in ghost_nodes_dict:
                    pacman_next_nodes.add((p_node[0],p_node[1],p_node[2]+"_"))
                    pacman_nodes_without_paths.add((p_node[0],p_node[1]))
                    path_dict[(p_node[0] , p_node[1])] = p_node[2] +"_"

                    if (p_node[0] , p_node[1]) < lowest_place_achieved:
                        lowest_place_achieved = (p_node[0] , p_node[1])
                        lowest_place_achieved_path = p_node[2] + "_"
                    elif (p_node[0] , p_node[1]) == lowest_place_achieved:
                        if p_node[2] + "_" < lowest_place_achieved_path:
                            lowest_place_achieved_path = p_node[2] + "_"
            # ghost_next_nodes = set()
            ghost_nodes_without_paths = set()

            for g_node in ghost_nodes:
                # down
                if g_node[0] + 1 < rows and maze[g_node[0] + 1][g_node[1]] != "X":
                    # ghost_next_nodes.add((g_node[0] + 1, g_node[1], g_node[2] + "D"))
                    ghost_nodes_without_paths.add((g_node[0] + 1, g_node[1]))
                    ghost_nodes_dict[(g_node[0] + 1, g_node[1])] = True
                # up
                if g_node[0] - 1 >= 0 and maze[g_node[0] - 1][g_node[1]] != "X":
                    # ghost_next_nodes.add((g_node[0] - 1, g_node[1], g_node[2] + "U"))
                    ghost_nodes_without_paths.add((g_node[0] - 1, g_node[1]))
                    ghost_nodes_dict[(g_node[0] - 1, g_node[1])] = True

                # right
                if g_node[1] + 1 < columns and maze[g_node[0]][g_node[1] + 1] != "X":
                    # ghost_next_nodes.add((g_node[0], g_node[1] + 1, g_node[2] + "R"))
                    ghost_nodes_without_paths.add((g_node[0], g_node[1] + 1))
                    ghost_nodes_dict[(g_node[0] , g_node[1] +1)] = True
                # up
                if g_node[1] - 1 >= 0 and maze[g_node[0]][g_node[1]-1] != "X":
                    # ghost_next_nodes.add((g_node[0], g_node[1] - 1, g_node[2] + "L"))
                    ghost_nodes_without_paths.add((g_node[0], g_node[1] - 1))
                    ghost_nodes_dict[(g_node[0] , g_node[1] - 1)] = True
            #
            pacman_nodes_set = pacman_nodes_without_paths
            ghost_nodes_set = set(ghost_nodes +list(ghost_nodes_without_paths))
            difference = pacman_nodes_set.difference(ghost_nodes_set)
            # pacman_nodes = list(set(list(pacman_next_nodes) +pacman_nodes))
            # # print("next_pacman",pacman_nodes,"ghost",ghost_nodes)
            # if len(difference) ==0:
            #     break
            #
            # pacman_nodes = list(pacman_next_nodes)
            # # print("next_pacman",pacman_nodes,"ghost",ghost_nodes)
            # if len(pacman_nodes) == 0:
            #     break
            # answer_strings = [nt[2] for nt in pacman_nodes]
            # ghost_nodes = list(ghost_nodes_set)
            # t+=1

            pacman_nodes = list(pacman_next_nodes)
            ghost_nodes_set = set(ghost_nodes + list(ghost_nodes_without_paths))
            # print("next_pacman",pacman_nodes,"ghost",ghost_nodes)
            if len(difference) ==0:
                break

            answer_strings = [nt[2] for nt in pacman_nodes]
            ghost_nodes = list(ghost_nodes_set)
            t += 1

        if t == 15:
            print("INFINITE",lowest_place_achieved)
        else:
            answer_strings.sort()
            print(t,answer_strings[0])
