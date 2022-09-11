# Challenge Name: Marc's Cakewalk
# Difficulty: Easy
from typing import List


def cake_walk(calorie: List[int]):
    answer = 0
    power = 1
    calorie.sort(reverse=True)
    for cal in calorie:
        answer += power * cal
        power *= 2
    return answer


print(cake_walk([1, 3, 2]))
