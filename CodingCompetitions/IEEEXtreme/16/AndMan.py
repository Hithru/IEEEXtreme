test_cases = int(input())

for t in range(test_cases):
    nodes = int(input())
    weights = list(map(int, input().strip().split()))
    nodes_leaves = {}

    for k in range(nodes - 1):
        n1, n2 = map(int, input().strip().split())
        nodes_leaves.setdefault(n1, [])
        nodes_leaves.setdefault(n2, [])
        nodes_leaves[n1].append(n2)
        nodes_leaves[n2].append(n1)
    q = int(input())

    for j in range(q):
        operation_type, start, end = map(int, input().split())
        if operation_type == 1:
            weights[start - 1] = end
        else:
            answer = 0
            already_included = {start: True}
            nodes_to_traverse = []
            for i in nodes_leaves[start]:
                nodes_to_traverse.append((i, weights[start - 1]))
                already_included.setdefault(i, True)

            while nodes_to_traverse:
                next_node, mul = nodes_to_traverse.pop(0)
                already_included.setdefault(next_node, True)
                next_mul = (mul * weights[next_node - 1]) % 1000000007
                if next_node == end:
                    answer = next_mul % 1000000007
                    break
                else:
                    for ed in nodes_leaves[next_node]:
                        if ed not in already_included:
                            nodes_to_traverse.append((ed, next_mul % 1000000007))
                            already_included.setdefault(ed, True)
        print(answer % 1000000007)
