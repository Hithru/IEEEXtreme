n, k = map(int, input().strip().split())
from queue import PriorityQueue

radius_list = []
for j in range(n):
    number = int(input().strip())
    radius_list.append(number)
radius_list.sort()

end_index = 0

priority_que = PriorityQueue()
maxi, answer = 0, 0

for rad in range(len(radius_list)):
    while end_index < len(radius_list) and radius_list[end_index] <= radius_list[rad] + k:
        end_index += 1

    difference = end_index - rad

    while not priority_que.empty():
        if priority_que.queue[0][0] > rad:
            break
        qu = priority_que.get()

        maxi = max(maxi, qu[1])
    answer = max(answer, maxi + difference)
    priority_que.put([end_index, difference])

print(answer)
