test_cases = int(input())

for t in range(test_cases):
    dinners = int(input())
    dinner_details = {}
    for j in range(dinners):
        details = input().split()
        dinner_details.setdefault(details[0], [0, 0])
        dinner_details[details[0]][0] += int(details[1])

        for k in range(int(details[1])):
            dinner_details.setdefault(details[2 + k], [0, 0])
            dinner_details[details[2 + k]][1] += 1

    print(dinner_details)

    treats_to_give = [val[1] - val[0] for val in dinner_details.values() if val[1] - val[0] > 0]
    treats_to_receive = [val[0] - val[1] for val in dinner_details.values() if val[0] - val[1] > 0]

    print("treats_to_give", treats_to_give)
    print("treats_to_receive", treats_to_receive)

    treats_to_give.sort(reverse=True)
    treats_to_receive.sort(reverse=True)
    days = 0
    g = 0
    answer_dinners = sum(treats_to_give)

    print(answer_dinners,max(treats_to_receive))
