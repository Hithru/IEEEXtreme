# Challenge Name: Fibonacci Numbers
# Difficulty: Easy

fibonacci_numbers = {0: 0, 1: 1}


def fibonacci(n):
    if n in fibonacci_numbers:
        return fibonacci_numbers[n]
    else:
        answer = fibonacci(n - 1) + fibonacci(n - 2)
        fibonacci_numbers[n] = answer
        return answer


n = int(input())
print(fibonacci(n))
