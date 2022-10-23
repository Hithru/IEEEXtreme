test_cases = int(input())

for test_case in range(1,test_cases+1):
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
        print("Case #"+str(test_case)+": "+ "INFINITE STAY")
    else:
        t = 0

        ghost_nodes = [(ghost_start[0],ghost_start[1],0)]
        ghost_node_achieve_time = {(ghost_start[0],ghost_start[1]):0}

        while len(ghost_nodes) > 0:
            g_node = ghost_nodes.pop(0)
            time = g_node[2] +1
            if g_node[0] + 1 < rows and maze[g_node[0] + 1][g_node[1]] != "X":
                # ghost_next_nodes.add((g_node[0] + 1, g_node[1], g_node[2] + "D"))
                if (g_node[0] + 1, g_node[1])not in ghost_node_achieve_time:
                    ghost_nodes.append((g_node[0] + 1, g_node[1],time))
                    ghost_node_achieve_time[(g_node[0] + 1, g_node[1])] = time
            # up
            if g_node[0] - 1 >= 0 and maze[g_node[0] - 1][g_node[1]] != "X":
                # ghost_next_nodes.add((g_node[0] - 1, g_node[1], g_node[2] + "U"))
                if (g_node[0] - 1, g_node[1]) not in ghost_node_achieve_time:
                    ghost_nodes.append((g_node[0] - 1, g_node[1],time))
                    ghost_node_achieve_time[(g_node[0] - 1, g_node[1])] = time

            # right
            if g_node[1] + 1 < columns and maze[g_node[0]][g_node[1] + 1] != "X":
                # ghost_next_nodes.add((g_node[0], g_node[1] + 1, g_node[2] + "R"))
                if (g_node[0], g_node[1] + 1) not in ghost_node_achieve_time:
                    ghost_nodes.append((g_node[0], g_node[1] + 1,time))
                    ghost_node_achieve_time[(g_node[0], g_node[1] + 1)] = time
            # up
            if g_node[1] - 1 >= 0 and maze[g_node[0]][g_node[1] - 1] != "X":
                # ghost_next_nodes.add((g_node[0], g_node[1] - 1, g_node[2] + "L"))
                if (g_node[0], g_node[1] - 1) not in ghost_node_achieve_time:
                    ghost_nodes.append((g_node[0], g_node[1] - 1,time))
                    ghost_node_achieve_time[(g_node[0], g_node[1] - 1)] = time
        # print(ghost_node_achieve_time)

        pacman_nodes = [(pacman_start[0], pacman_start[1], 0, "")]
        packman_node_achieve_time = {(ghost_start[0], ghost_start[1]): 0}
        packman_node_achieve_path = {(ghost_start[0], ghost_start[1]): ""}
        infinite_nodes = []
        while len(pacman_nodes) > 0:
            p_node = pacman_nodes.pop(0)
            time = p_node[2] + 1
            path = p_node[3]
            if time == 5:
                break
            # left
            if p_node[1] - 1 >= 0 and maze[p_node[0]][p_node[1] - 1] != "X":
                # ghost_next_nodes.add((g_node[0] + 1, g_node[1], g_node[2] + "D"))
                if (p_node[0], p_node[1] - 1) not in packman_node_achieve_time:
                    if (p_node[0], p_node[1] - 1) not in ghost_node_achieve_time:
                        pacman_nodes.append((p_node[0], p_node[1] - 1, time, path + "L"))
                        packman_node_achieve_time[(p_node[0], p_node[1] - 1)] = time
                        packman_node_achieve_path[(p_node[0], p_node[1] - 1)] = path + "L"
                        infinite_nodes.append((p_node[0], p_node[1] - 1))
                    else:
                        if time < ghost_node_achieve_time[(p_node[0], p_node[1] - 1)]:
                            pacman_nodes.append((p_node[0], p_node[1] - 1, time, path + "L"))
                            packman_node_achieve_time[(p_node[0], p_node[1] - 1)] = time
                            packman_node_achieve_path[(p_node[0], p_node[1] - 1)] = path + "L"
            # path = p_node[3]

            # up
            if p_node[0] - 1 >= 0 and maze[p_node[0] - 1][p_node[1]] != "X":
                # ghost_next_nodes.add((g_node[0] + 1, g_node[1], g_node[2] + "D"))
                if (p_node[0] - 1, p_node[1]) not in packman_node_achieve_time:
                    if (p_node[0] - 1, p_node[1]) not in ghost_node_achieve_time:
                        pacman_nodes.append((p_node[0] - 1, p_node[1], time, path + "U"))
                        packman_node_achieve_time[(p_node[0] - 1, p_node[1])] = time
                        packman_node_achieve_path[(p_node[0] - 1, p_node[1])] = path + "U"
                        infinite_nodes.append((p_node[0] - 1, p_node[1]))
                    else:
                        if time < ghost_node_achieve_time[(p_node[0] - 1, p_node[1])]:
                            pacman_nodes.append((p_node[0] - 1, p_node[1], time, path + "U"))
                            packman_node_achieve_time[(p_node[0] - 1, p_node[1])] = time
                            packman_node_achieve_path[(p_node[0] - 1, p_node[1])] = path + "U"

            # right

            if p_node[1] + 1 < columns and maze[p_node[0]][p_node[1] + 1] != "X":
                # ghost_next_nodes.add((g_node[0] + 1, g_node[1], g_node[2] + "D"))
                if (p_node[0], p_node[1] + 1) not in packman_node_achieve_time:
                    if (p_node[0], p_node[1] + 1) not in ghost_node_achieve_time:
                        pacman_nodes.append((p_node[0], p_node[1] + 1, time, path + "R"))
                        packman_node_achieve_time[(p_node[0], p_node[1] + 1)] = time
                        packman_node_achieve_path[(p_node[0], p_node[1] + 1)] = path + "R"
                        infinite_nodes.append((p_node[0], p_node[1] + 1))
                    else:
                        if time < ghost_node_achieve_time[(p_node[0], p_node[1] + 1)]:
                            pacman_nodes.append((p_node[0], p_node[1] + 1, time, path + "R"))
                            packman_node_achieve_time[(p_node[0], p_node[1] + 1)] = time
                            packman_node_achieve_path[(p_node[0], p_node[1] + 1)] = path + "R"

            # down
            if p_node[0] + 1 < rows and maze[p_node[0] + 1][p_node[1]] != "X":
                # ghost_next_nodes.add((g_node[0] + 1, g_node[1], g_node[2] + "D"))
                if (p_node[0] + 1, p_node[1]) not in packman_node_achieve_time:
                    if (p_node[0] + 1, p_node[1]) not in ghost_node_achieve_time:
                        pacman_nodes.append((p_node[0] + 1, p_node[1], time, path + "D"))
                        packman_node_achieve_time[(p_node[0] + 1, p_node[1])] = time
                        packman_node_achieve_path[(p_node[0] + 1, p_node[1])] = path + "D"
                        infinite_nodes.append((p_node[0] + 1, p_node[1]))
                    else:
                        if time < ghost_node_achieve_time[(p_node[0] + 1, p_node[1])]:
                            pacman_nodes.append((p_node[0] + 1, p_node[1], time, path + "D"))
                            packman_node_achieve_time[(p_node[0] + 1, p_node[1])] = time
                            packman_node_achieve_path[(p_node[0] + 1, p_node[1])] = path + "D"
            # stay
        # print("start_node", pacman_start, max(packman_node_achieve_time.values()), packman_node_achieve_time)
        # print(packman_node_achieve_path)
        infinite_nodes.sort()
        # print(infinite_nodes)

        if len(infinite_nodes) > 0:
            print("Case #" + str(test_case) + ": " + "INFINITE" + " " + packman_node_achieve_path[infinite_nodes[0]])
        else:
            pacman_nodes = [(pacman_start[0], pacman_start[1], 0, "")]
            # packman_node_achieve_time = {(ghost_start[0], ghost_start[1]): 0}
            # packman_node_achieve_path = {(ghost_start[0], ghost_start[1]): ""}

            while len(pacman_nodes) > 0:
                p_node = pacman_nodes.pop(0)
                time = p_node[2] + 1
                path = p_node[3]
                if time == 16:
                    break
                # left
                if p_node[1] - 1 >= 0 and maze[p_node[0]][p_node[1] - 1] != "X":
                    # ghost_next_nodes.add((g_node[0] + 1, g_node[1], g_node[2] + "D"))

                    if (p_node[0], p_node[1] - 1) not in ghost_node_achieve_time:
                        pacman_nodes.append((p_node[0], p_node[1] - 1, time, path + "L"))
                        packman_node_achieve_time[(p_node[0], p_node[1] - 1)] = time
                        packman_node_achieve_path[(p_node[0], p_node[1] - 1)] = path + "L"

                    else:
                        if time < ghost_node_achieve_time[(p_node[0], p_node[1] - 1)]:
                            pacman_nodes.append((p_node[0], p_node[1] - 1, time, path + "L"))
                            packman_node_achieve_time[(p_node[0], p_node[1] - 1)] = time
                            packman_node_achieve_path[(p_node[0], p_node[1] - 1)] = path + "L"
                # path = p_node[3]

                # up
                if p_node[0] - 1 >= 0 and maze[p_node[0] - 1][p_node[1]] != "X":
                    # ghost_next_nodes.add((g_node[0] + 1, g_node[1], g_node[2] + "D"))

                    if (p_node[0] - 1, p_node[1]) not in ghost_node_achieve_time:
                        pacman_nodes.append((p_node[0] - 1, p_node[1], time, path + "U"))
                        packman_node_achieve_time[(p_node[0] - 1, p_node[1])] = time
                        packman_node_achieve_path[(p_node[0] - 1, p_node[1])] = path + "U"

                    else:
                        if time < ghost_node_achieve_time[(p_node[0] - 1, p_node[1])]:
                            pacman_nodes.append((p_node[0] - 1, p_node[1], time, path + "U"))
                            packman_node_achieve_time[(p_node[0] - 1, p_node[1])] = time
                            packman_node_achieve_path[(p_node[0] - 1, p_node[1])] = path + "U"

                # right

                if p_node[1] + 1 < columns and maze[p_node[0]][p_node[1] + 1] != "X":
                    # ghost_next_nodes.add((g_node[0] + 1, g_node[1], g_node[2] + "D"))

                    if (p_node[0], p_node[1] + 1) not in ghost_node_achieve_time:
                        pacman_nodes.append((p_node[0], p_node[1] + 1, time, path + "R"))
                        packman_node_achieve_time[(p_node[0], p_node[1] + 1)] = time
                        packman_node_achieve_path[(p_node[0], p_node[1] + 1)] = path + "R"

                    else:
                        if time < ghost_node_achieve_time[(p_node[0], p_node[1] + 1)]:
                            pacman_nodes.append((p_node[0], p_node[1] + 1, time, path + "R"))
                            packman_node_achieve_time[(p_node[0], p_node[1] + 1)] = time
                            packman_node_achieve_path[(p_node[0], p_node[1] + 1)] = path + "R"

                # down
                if p_node[0] + 1 < rows and maze[p_node[0] + 1][p_node[1]] != "X":
                    # ghost_next_nodes.add((g_node[0] + 1, g_node[1], g_node[2] + "D"))

                    if (p_node[0] + 1, p_node[1]) not in ghost_node_achieve_time:
                        pacman_nodes.append((p_node[0] + 1, p_node[1], time, path + "D"))
                        packman_node_achieve_time[(p_node[0] + 1, p_node[1])] = time
                        packman_node_achieve_path[(p_node[0] + 1, p_node[1])] = path + "D"

                    else:
                        if time < ghost_node_achieve_time[(p_node[0] + 1, p_node[1])]:
                            pacman_nodes.append((p_node[0] + 1, p_node[1], time, path + "D"))
                            packman_node_achieve_time[(p_node[0] + 1, p_node[1])] = time
                            packman_node_achieve_path[(p_node[0] + 1, p_node[1])] = path + "D"
                # stay
                if (p_node[0], p_node[1]) not in ghost_node_achieve_time:
                    pacman_nodes.append((p_node[0], p_node[1], time, path))
                    packman_node_achieve_time[(p_node[0], p_node[1])] = time
                    packman_node_achieve_path[(p_node[0], p_node[1])] = path
                else:
                    if time < ghost_node_achieve_time[(p_node[0], p_node[1])]:
                        pacman_nodes.append((p_node[0], p_node[1], time, path))
                        packman_node_achieve_time[(p_node[0], p_node[1])] = time
                        packman_node_achieve_path[(p_node[0], p_node[1])] = path

            max_value = max(packman_node_achieve_time.values())
            max_value_keys = [key for key,value in packman_node_achieve_time.items() if value == max_value]
            max_value_keys.sort()
            print("Case #"+str(test_case)+": "+str(max_value)+" "+packman_node_achieve_path[max_value_keys[0]])

