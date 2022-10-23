


def minimum_price(current_station, next_station, tank_left, distance_left, final_station, tank_size):
    if distance_left == 0:
        return 0
    elif (current_station, next_station, tank_left, distance_left, final_station, tank_size) in dynamic_list:
        return dynamic_list[(current_station, next_station, tank_left, distance_left, final_station, tank_size)]
    elif next_station == final_station-1:
        if tank_left >= stations_data[next_station][0]:
            return 0
        else:
            return 500 + (tank_size - tank_left) * stations_data[current_station][1]
    else:

        take_full_tank = (tank_size - tank_left) * stations_data[current_station][1] + 500 + minimum_price(
            current_station + 1, next_station + 1, tank_size - stations_data[next_station][0],
            distance_left - stations_data[next_station][0], final_station, tank_size)

        if tank_left >= stations_data[next_station][0]:
            go_without_filling = minimum_price(current_station + 1, next_station + 1,
                                               tank_left - stations_data[next_station][0],
                                               distance_left - stations_data[next_station][0], final_station,
                                               tank_size)
            answer = min(go_without_filling, take_full_tank)
        else:
            answer = take_full_tank
        # print(current_station,next_station, answer)
        dynamic_list[(current_station, next_station, tank_left, distance_left, final_station, tank_size)] = answer
        return answer

test_cases = int(input())
for t in range(test_cases):
    stations, tank_size, fuel_price = map(int, input().strip().split())
    stations_data = []
    distance_left = 0
    for k in range(stations):
        distance, price = map(int, input().strip().split())
        distance_left += distance
        stations_data.append((distance, price))
    price = tank_size * fuel_price
    dynamic_list = {}
    if len(stations_data) > 1:
        next_prices = minimum_price(0, 1, tank_size - stations_data[0][0], distance_left - stations_data[0][0],
                                    stations, tank_size)

        # print(price,next_prices,price )
        print(price + next_prices)
    else:
        print(price)