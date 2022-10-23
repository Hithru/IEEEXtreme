n, p = map(int, input().strip().split(" "))
nodes = {}
root_node = []
already_added = {}
leafs = {}
for i in range(n):
    node_details = input().strip().split()
    if len(node_details) == 5:
        # internal node
        # node = {type,character,leafs[yes],leafs[no]
        nodes[node_details[1]] = (node_details[0], node_details[2], node_details[3], node_details[4])
        if node_details[1] not in already_added:
            root_node.append(node_details[1])
            already_added.setdefault(node_details[1], True)
        if node_details[3] not in already_added:
            root_node.append(node_details[3])
            already_added.setdefault(node_details[3], True)
        if node_details[4] not in already_added:
            root_node.append(node_details[4])
            already_added.setdefault(node_details[4], True)
        if node_details[3] not in leafs:
            leafs.setdefault(node_details[3], True)
            root_node.remove(node_details[3])
        if node_details[4] not in leafs:
            leafs.setdefault(node_details[4], True)
            root_node.remove(node_details[4])
    elif len(node_details) == 3:
        # leaf node
        # node = {type,langauge}
        nodes[node_details[1]] = (node_details[0], node_details[2])
        if node_details[1] not in already_added:
            root_node.append(node_details[1])
            already_added.setdefault(node_details[1], True)
        if node_details[1] not in leafs:
            leafs.setdefault(node_details[1], True)
            root_node.remove(node_details[1])


for j in range(p):
    string = input()

    nodes_to_traverse = [root_node[0]]
    answer = []
    while nodes_to_traverse:
        node = nodes_to_traverse.pop(0)
        character = nodes[node][1]
        if character in string:
            yes_node = nodes[node][2]
            if nodes[yes_node][0] == "L":
                answer.append(nodes[yes_node][1])
            else:
                nodes_to_traverse.append(yes_node)
        else:
            yes_node = nodes[node][2]
            if nodes[yes_node][0] == "L":
                answer.append(nodes[yes_node][1])
            else:
                nodes_to_traverse.append(yes_node)
            no_node = nodes[node][3]
            if nodes[no_node][0] == "L":
                answer.append(nodes[no_node][1])
            else:
                nodes_to_traverse.append(no_node)

    answer.sort()
    print(" ".join(answer))

