from datetime import datetime


# from cs1033_evaluator import evaluate_lab7

def days_to_birthday(date):
    '''
    Calculates the number of days that have passed since the 1st of January
    to the given date.

    :param date: A date string in the format of yyyy-mm-dd
    :return: The number of days to the date from 1st of January
             (eg: date->2021-01-01, return->1)
    '''

    # Convert the date string to a datetime object
    datetime_object = datetime.strptime(date, "%Y-%m-%d")

    # Extract only the date and remove the timestamp
    date = datetime_object.date()

    # Find the number of days since the begining of the year
    num_days = date.timetuple().tm_yday

    return num_days


# Please do not edit anything above this line.
################################################################################


# Your code should be included here.
# You may use the days_to_birthday(date) function in your solution.
file_name = input()
with open(file_name) as details:
    output_file_context = []
    birth_year_submissions = {}
    for line in details:
        name, date, gender = line.strip().split()
        year, month, day = date.strip().split("-")
        birth_year_submissions.setdefault(year, 0)
        birth_year_submissions[year] += 1
        print(date)
        days = days_to_birthday(date)
        if gender == "F":
            days += 500
        output_line = name + " " + year + (3 - len(str(days))) * "0" + str(days) + (
                    3 - len(str(birth_year_submissions[year]))) * "0" + str(birth_year_submissions[year])

        output_file_context.append(output_line)

    with open("outfile.txt", "w") as outfile:
        outfile.write("\n".join(output_file_context))

################################################################################
# Please do not edit anything below this line.
# evaluate_lab7()

##################### End of the programme #####################################
