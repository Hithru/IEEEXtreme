# Python3 program for the above approach

# Function to calculate the minimum cost
# required to reach the end of Line
def minCost(N, K, M, a, b,tank_size):

    map = {}
    for i in range(M):
        map[a[i]] = b[i]

    # Stores the station index and cost of fuel and
    # litres of petrol which is being fueled
    pq = []
    cost = 0
    flag = False

    # Iterate through the entire line
    for i in range(N):

        # Check if there is a station at current index
        if (i in map):
            arr = [i, map[i], 0]
            pq.append(arr)

        pq.sort()

        # Remove all the stations where
        # fuel cannot be pumped
        while (len(pq) > 0 and pq[-1][2] == K):
            pq.pop()


        # Stores the best station
        # visited so far
        best_bunk = pq[len(pq) - 1]
        pq.pop()

        # Pump fuel from the best station
        cost += best_bunk[1]

        # Update the count of litres
        # taken from that station
        best_bunk[2] += 1

        # Update the bunk in queue
        pq.append(best_bunk)
        pq.sort()



    # Print the cost
    print(cost)


test_cases = int(input())
for t in range(test_cases):
    stations, tank_size, fuel_price = map(int, input().strip().split())
    stations_data = []
    distance_left = 0
    a = [0]
    b = [fuel_price]
    for k in range(stations):
        distance, price = map(int, input().strip().split())
        distance_left += distance
        stations_data.append((distance, price))
        a.append(distance_left)
        b.append(price)

    # Driven Program
    # Given value of N, K & M
    N, K, M = distance_left, tank_size, len(a)

    print(N, K, M, a, b)
    # Function call to calculate minimum
    # cost to reach end of the line
    minCost(N, K, M, a, b,tank_size)
