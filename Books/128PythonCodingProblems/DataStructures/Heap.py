class OurHeap:
    def __init__(self, items):
        self.heap = [None]
        self.rank = {}
        for x in items:
            self.push(x)

    def __len__(self):
        return len(self.heap)

    def push(self, x):
        assert x not in self.rank
        i = len(self.heap)
        self.heap.append(x)
        self.rank[x] = i
        self.up(i)

    def pop(self):
        root = self.heap[1]
        del self.rank[root]
        x = self.heap.pop()
        if len(self.rank) > 0:
            self.heap[1] = x
            self.rank[x] = 1
            self.down(1)
        return root

    def up(self, i):
        x = self.heap[i]
        while i > 1 and x < self.heap[i // 2]:
            self.heap[i] = self.heap[i // 2]
            self.rank[self.heap[i // 2]] = i
            i //= 2
        self.heap[i] = x
        self.rank[x] = i

    def down(self, i):
        x = self.heap[i]
        n = len(self.heap)

        while True:
            left = 2 * i
            right = left + 1
            if right < n and self.heap[right] < x and self.heap[right] < self.heap[left]:
                self.heap[i] = self.heap[right]
                self.rank[self.heap[right]] = i
                i = right
            elif left < n and self.heap[left] < x:
                self.heap[i] = self.heap[left]
                self.rank[self.heap[left]] = i
                i = left
            else:
                self.heap[i] = x
                self.rank[x] = i
                return

    def update(self, old, new):
        i = self.rank[old]
        del self.rank[old]
        self.heap[i] = new
        self.rank[new] = i
        if old < new:
            self.down(i)
        else:
            self.up(i)


priority_heap = OurHeap([3, 43, 25, 45, 363, 2])
print(priority_heap.pop())
print(priority_heap.pop())
print(priority_heap.pop())
print(priority_heap.pop())
print(priority_heap.pop())
print(priority_heap.pop())
