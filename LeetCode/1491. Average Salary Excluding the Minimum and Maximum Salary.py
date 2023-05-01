# Problem Number: 1491
# Problem Name: Average Salary Excluding the Minimum and Maximum Salary
# Difficulty: Easy
from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        maximum = salary[0]
        minimum = salary[1]
        if salary[0] < salary[1]:
            maximum,minimum = minimum,maximum

        total = maximum + minimum
        for i in range(2,len(salary)):
            total += salary[i]
            if salary[i] > maximum:
                maximum = salary[i]
            if salary[i] < minimum:
                minimum = salary[i]

        total -=(maximum + minimum)

        answer = total/(len(salary)-2)

        return answer