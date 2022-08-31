class UnionFind:
    def __init__(self, n):
        self.up_bound = list(range(n))
        self.rank = [0] * n

    def find(self, x_index):
        print(self.up_bound, self.rank)
        if self.up_bound[x_index] == x_index:
            return x_index

        self.up_bound[x_index] = self.find(self.up_bound[x_index])

        return self.up_bound[x_index]

    def union(self, x_index, y_index):
        repr_x = self.find(x_index)
        repr_y = self.find(y_index)

        if repr_x == repr_y:
            return False

        if self.rank[repr_x] == self.rank[repr_y]:
            self.rank[repr_x] += 1
            self.up_bound[repr_y] = repr_x
        elif self.rank[repr_x] > self.rank[repr_y]:
            self.up_bound[repr_y] = repr_x
        else:
            self.up_bound[repr_x] = repr_y

        return True


new_union = UnionFind(10)
new_union.union(9, 8)
print(new_union.find(9))
print(new_union.find(8))
