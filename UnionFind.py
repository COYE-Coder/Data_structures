# Naive Implementation of Union Find

class UnionFind:
    # First define a data structure
    def __init__(self, size, two_dim=False):
        self.size = size
        self.two_dim = False
        if two_dim:
            self.d_structure = [i for i in range(size)]
        self.d_structure = [i for i in range(size)]

    def is_connected(self, p, q):
        return self.d_structure[p] == self.d_structure[q]

    # Note poor efficiency
    def union(self, p, q):
        old_p = self.d_structure[p]
        old_q = self.d_structure[q]
        for i in range(self.size):
            if self.d_structure[i] == old_p:
                self.d_structure[q] = old_p

    def display(self):
        print(self.d_structure)


test = UnionFind(10)
test.display()

test.union(2, 3)
test.display()

test.union(2, 5)
test.display()
