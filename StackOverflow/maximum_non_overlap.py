n, k = map(int, input().split())
from queue import PriorityQueue


def non_overlapping_answer(interval):
    priority_que = PriorityQueue()
    maxi, answer = 0, 0
    interval.sort()
    for element in interval:
        while not priority_que.empty():
            if priority_que.queue[0][0] >= element[0]:
                break
            qu = priority_que.get()

            maxi = max(maxi, qu[1])
        answer = max(answer, maxi + element[2])
        priority_que.put([element[1], element[2]])

    return answer


radius_list = []
for j in range(n):
    radius_list.append(int(input()))
radius_list.sort()

intervals = []

end_index = 0

for rad in range(len(radius_list)):
    while end_index < len(radius_list) and radius_list[end_index] <= radius_list[rad] + k:
        end_index += 1
    intervals.append([rad, end_index, end_index - rad])

maxValue = non_overlapping_answer(intervals)
print(maxValue)
