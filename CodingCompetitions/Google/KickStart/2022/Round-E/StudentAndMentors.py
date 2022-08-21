test_cases = int(input())

for t in range(test_cases):
    number_of_students = int(input())
    students_rating = [int(i) for i in input().split()]
    mentor_condition = sorted([(2*students_rating[i],i) for i in range(len(students_rating))],reverse=True)
    mentors = sorted([(students_rating[i],i) for i in range(len(students_rating))],reverse=True)
    answers = [None for i in range(number_of_students)]

    for start_index in range(len(mentors)):
        i = 0
        while i < len(mentors):
            if mentors[i][0] <= mentor_condition[start_index][0]:
                if mentors[i][1] == mentor_condition[start_index][1]:
                    pass
                else:
                    answers[mentor_condition[start_index][1]] = str(mentors[i][0])
                    break
            i +=1
        else:
            answers[mentor_condition[start_index][1]] = str("-1")



    print("Case #{}: {}".format(t + 1, " ".join(answers)))