test_cases = int(input())

for test_case in range(test_cases):
    rows, columns = map(int, input().strip().split())
    maze = []
    pacman_start = (-1, -1)
    ghost_start = (-1, -1)
    for k in range(rows):
        r = input()
        row = []
        for i in range(len(r)):
            row.append(r[i])
            if r[i] == "P":
                pacman_start = (k, i)
            if r[i] == "G":
                ghost_start = (k, i)
        maze.append(row)
    if ghost_start == (-1, -1):
        print("INFINITE STAY")
    else:

        t = 0
        pacman_nodes = [(pacman_start[0], pacman_start[1], "")]
        ghost_nodes = [(ghost_start[0], ghost_start[1])]
        ghost_nodes_dict = {(ghost_start[0], ghost_start[1]): True}
        answer = ""
        answer_strings = []
        while t < 30 and len(pacman_nodes) > 0:
            pacman_next_nodes = set()
            pacman_nodes_without_paths = set()
            path_dict = {}
            for p_node in pacman_nodes:

                # down
                if p_node[0] + 1 < rows and maze[p_node[0] + 1][p_node[1]] != "X" and (
                        len(p_node[2]) == 0 or p_node[2][-1] != "U") and (
                p_node[0] + 1, p_node[1]) not in ghost_nodes_dict:
                    pacman_next_nodes.add((p_node[0] + 1, p_node[1], p_node[2] + "D"))
                    pacman_nodes_without_paths.add((p_node[0] + 1, p_node[1]))
                    path_dict[(p_node[0] + 1, p_node[1])] = p_node[2] + "D"
                # up
                if p_node[0] - 1 >= 0 and maze[p_node[0] - 1][p_node[1]] != "X" and (
                        len(p_node[2]) == 0 or p_node[2][-1] != "D") and (
                p_node[0] - 1, p_node[1]) not in ghost_nodes_dict:
                    pacman_next_nodes.add((p_node[0] - 1, p_node[1], p_node[2] + "U"))
                    pacman_nodes_without_paths.add((p_node[0] - 1, p_node[1]))
                    path_dict[(p_node[0] - 1, p_node[1])] = p_node[2] + "U"

                # right
                if p_node[1] + 1 < columns and maze[p_node[0]][p_node[1] + 1] != "X" and (
                        len(p_node[2]) == 0 or p_node[2][-1] != "L") and (
                p_node[0], p_node[1] + 1) not in ghost_nodes_dict:
                    pacman_next_nodes.add((p_node[0], p_node[1] + 1, p_node[2] + "R"))
                    pacman_nodes_without_paths.add((p_node[0], p_node[1] + 1))
                    path_dict[(p_node[0], p_node[1] + 1)] = p_node[2] + "R"
                # up
                if p_node[1] - 1 >= 0 and maze[p_node[0]][p_node[1] - 1] != "X" and (
                        len(p_node[2]) == 0 or p_node[2][-1] != "R") and (
                p_node[0], p_node[1] - 1) not in ghost_nodes_dict:
                    pacman_next_nodes.add((p_node[0], p_node[1] - 1, p_node[2] + "L"))
                    pacman_nodes_without_paths.add((p_node[0], p_node[1] - 1))
                    path_dict[(p_node[0], p_node[1] - 1)] = p_node[2] + "L"


            # ghost_next_nodes = set()
            ghost_nodes_without_paths = set()
            ghost_nodes_dict = {}
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
                    ghost_nodes_dict[(g_node[0], g_node[1] + 1)] = True
                # up
                if g_node[1] - 1 >= 0 and maze[g_node[0]][g_node[1] - 1] != "X":
                    # ghost_next_nodes.add((g_node[0], g_node[1] - 1, g_node[2] + "L"))
                    ghost_nodes_without_paths.add((g_node[0], g_node[1] - 1))
                    ghost_nodes_dict[(g_node[0], g_node[1] - 1)] = True

            pacman_nodes = list(pacman_next_nodes)
            # print("next_pacman",pacman_nodes,"ghost",ghost_nodes)
            if len(pacman_nodes) == 0:
                break
            answer_strings = [nt[2] for nt in pacman_nodes]
            ghost_nodes = list(ghost_nodes_without_paths)
            t += 1

        if len(answer_strings) > 0:
            answer_strings.sort()
            print(len(answer_strings[0]), answer_strings[0])
        else:
            print("No_strings")
