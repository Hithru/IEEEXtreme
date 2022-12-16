# Problem Number: 232
# Problem Name: Implement Queue using Stacks
# Difficulty: Easy
class MyQueue:

    def __init__(self):
        self.start_stack = []
        self.end_stack = []

    def push(self, x: int) -> None:
        self.start_stack.append(x)
        print(self.start_stack, self.end_stack)
        return

    def pop(self) -> int:
        if len(self.end_stack) == 0:
            self.end_stack = self.start_stack[::-1]
            self.start_stack = []
        return self.end_stack.pop()

    def peek(self) -> int:
        if len(self.end_stack) == 0:
            self.end_stack = self.start_stack[::-1]
            self.start_stack = []
        print(self.start_stack, self.end_stack)
        return self.end_stack[-1]

    def empty(self) -> bool:
        if len(self.end_stack) == 0:
            self.end_stack = self.start_stack[::-1]
            self.start_stack = []
        return len(self.end_stack) == 0

# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
x = 1
obj.push(x)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()