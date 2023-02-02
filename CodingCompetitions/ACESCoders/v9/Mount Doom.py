# Enter your code here. Read input from STDIN. Print output to STDOUTt
t = int(input())


def countDoom(node):
    if node in table:
        return table[node]
    else:
        answer = 0
        for k in connected_errupt[node]:
            answer += 1
            answer += countDoom(k)
        table[node] = answer
        return answer


for i in range(t):
    n = int(input())

    power = list(map(int, input().strip().split()))

    num_errupt = {i: 0 for i in range(1, n + 1)}

    connected_errupt = {i: [] for i in range(1, n + 1)}

    for i in range(n - 1):
        s, e = map(int, input().strip().split())

        if power[s - 1] < power[e - 1]:
            connected_errupt[e].append(s)
        elif power[e - 1] < power[s - 1]:
            connected_errupt[s].append(e)

    table = {}
    max_errupt_node = 0
    max_errupt = 0
    for j in range(1, n + 1):
        errupt = countDoom(j) + 1
        if errupt > max_errupt:
            max_errupt = errupt
            max_errupt_node = j
    print(max_errupt_node, max_errupt)
