# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class UnionFind(size, two_dim=False):
    # First define a data structure
    def __init__(self):
        self.size = size
        if two_dim:
            self.d_structure = [i for i in range(size)]
        self.d_structure = [i for i in range(size)]

    def is_connected(self,p,q):
        return self.d_structure[p] == self.d_structure[q]

    def union(self,p,q):
        self.d_structure[p] = self.d_structure[q]

    def display(self):
        print(self.d_structure)




test = UnionFind(10)
test.display()
print("Hello world'")
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Hello world")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
