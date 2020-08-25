# Smarter Implementation of Union Find- uses the "Quick Union" algorithm

class UnionFind:
    # First define a data structure
    def __init__(self, size, two_dim=False):
        self.size = size
        self.two_dim = False
        if two_dim:
            self.d_structure = [i for i in range(size)]
        self.d_structure = [i for i in range(size)]

    def is_connected(self, p, q):
        return self.get_root(p) == self.get_root[q]

    def get_root(self, p):
        while self.d_structure[p] != p:
            p = self.d_structure[p]
        return p

    def union(self, p, q):
        root_p = self.get_root(p)
        root_q = self.get_root(q)
        if root_p != root_q:
            self.d_structure[root_p] = self.d_structure[root_q]

    def display(self):
        print(self.d_structure)


test = UnionFind(10)
test.display()

test.union(2, 3)
test.display()

test.union(2, 5)
test.display()
