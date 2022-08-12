# Challenge Name: Fibonacci Modified
# Difficulty: Medium

def fibonacci_modified(index: int):
    if index in fibonacci_number:
        return fibonacci_number[index]
    else:
        answer = fibonacci_modified(index - 2) + fibonacci_modified(index - 1) ** 2
        fibonacci_number[index] = answer
        return answer


fibonacci_number = {1: 0, 2: 1}
print(fibonacci_modified(5))
