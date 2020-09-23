"""
Binary heap implementation of priority queue.
Class functions:
    - Heapify -> Create a "heaped" array from unheaped array
        Ex:
         arr = [8,3,2,7,9,1,4]
                 8
               /   \
              3	    2
             / \   / \
            7   9 1   4
        returns:
             [9, 8, 4, 3, 7, 1, 2]
                 9
               /   \
              8	    4
             / \   / \
            3   7 1   2
    - insert -> Insert an element into the correct spot in the heap
    - del_max -> deletes the maximum value, optionally returning the value
"""


class Heap:

    def __init__(self, arr, heap=None):
        self.arr = arr
        self.heap = [None] * (len(self.arr) + 1)

    def heapify(self):
        for a in self.arr:
            self.insert(a)

        return self.heap

    def insert(self, num):

        i = self._find_end()

        self.heap[i] = num
        j = i

        # Perform "Swim" action:
        while j > 1 and (self.heap[j // 2] < self.heap[j]):
            self._exch(j // 2, j)
            j = j // 2

    def del_max(self, return_max=False):
        i = self._find_end()

        print(i)
        # First switch the root with the end, storing the maximum

        max_value = self.heap[1]
        self._exch(1, i - 1)

        # Set the end to none to delete the maximum
        self.heap[i - 1] = None

        j = 1
        # Perform "sink" action:
        while j < i and (self.heap[j] < self.heap[j * 2]):
            # Exchange with "child" this time, but only with the superior child

            #  Check which is "superior"
            left_child_ind = (j * 2)
            right_child_ind = (j * 2) + 1

            if self.heap[left_child_ind] < self.heap[right_child_ind]:
                self._exch(j, right_child_ind)
                j = right_child_ind
            else:
                self._exch(j, left_child_ind)
                j = left_child_ind

        if return_max:
            return max_value

    # Helper functions that allow for exchanges, finding ends, etc

    def _exch(self, i, j):
        # Exchanges an element with its parent
        old_parent = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = old_parent

    def _find_end(self):
        # Find the "end" of the heap

        i = 1
        while self.heap[i] is not None:
            i += 1
            # Doubles the size of the array if needed:

            if i == len(self.heap):
                self._double()

        return i

    def _double(self):
        new_space = [None] * (len(self.heap) + 1)
        self.heap.extend(new_space)


# TESTING:

heap = Heap([8, 3, 2, 1, 1, 1, 4])

heap.heapify()
print(heap.heap)

heap.del_max()
print(heap.heap)
