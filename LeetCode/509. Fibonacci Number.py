# Problem Number: 509
# Problem Name: Fibonacci number
# Difficulty: Easy
class Solution:
    fibonacci_store = {0:0,1:1}
    def fib(self, n: int) -> int:

        if n in self.fibonacci_store:
            return self.fibonacci_store[n]
        else:
            answer = self.fib(n-1) + self.fib(n-2)
            self.fibonacci_store[n] = answer
            return answer