# Challenge Name: A Tale of Two Stacks
# Difficulty: Medium

class MyQueue(object):
    def __init__(self):
        self.lifo = []
        self.fifo = []

    def peek(self):
        if len(self.fifo) == 0:
            self.fifo = self.lifo[::-1]
            self.lifo = []
        return self.fifo[-1]

    def pop(self):
        if len(self.fifo) == 0:
            self.fifo = self.lifo[::-1]
            self.lifo = []
        return self.fifo.pop()

    def put(self, value):
        self.lifo.append(value)


queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())