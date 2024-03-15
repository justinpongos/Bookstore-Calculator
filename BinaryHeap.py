import numpy as np
import math
from Interfaces import Queue
from Interfaces import Tree


def left(i: int) -> int:
    """
    helper method; returns the index of the left child of the element at index i
    """
    # todo
    return 2 * i + 1

def right(i: int) -> int:
    """
    helper method; returns the index of the right child of the element at index i
    """
    # todo
    return 2 * (i + 1)

def parent(i: int) -> int:
    """
    helper method; returns the index of the parent of the element at index i
    """
    # todo
    return (i - 1) // 2

def _new_array(n: int) -> np.array:
    """
    helper method; creates a new numpy array of 0's of size n
    """
    return np.zeros(n, object)


class BinaryHeap(Queue, Tree):
    def __init__(self):
        self.a = _new_array(1)
        self.n = 0

    def add(self, x: object):
        # todo
        if len(self.a) == self.n:
            self._resize()
        self.a[self.n] = x
        self.n += 1
        self._bubble_up_last()
        return True

    def remove(self):
        # todo
        if self.n == 0:
            raise IndexError()
        x = self.a[0]
        self.a[0] = self.a[self.n - 1]
        self.n -= 1
        self._trickle_down_root()
        if 3 * self.n < len(self.a):
            self._resize()
        return x
                  
    def depth(self, u) -> int:
        # todo
        if u == None:
            raise ValueError(f'{u} is not found in the binary tree.')
        d = 0
        i = np.where(self.a == u)[0]
        while i > 0:
            i = parent(i)
            d += 1
        return d

    def height(self) -> int:
        # todo
        return int(math.log2(self.size()))

    def bf_order(self) -> list:
        # todo
        nodes = []
        for i in self.a:
          if i != 0:
            nodes.append(i)
        return nodes

    def in_order(self) -> list:
        return self._in_order(0)
  
    def _in_order(self, u) -> list:
        # todo
        nodes = []
        if left(u) < self.size() and self.a[left(u)] != None:
            nodes.extend(self._in_order(left(u)))
        nodes.append(self.a[u])
        if right(u) < self.size() and self.a[right(u)] != None:
            nodes.extend(self._in_order(right(u)))
        return nodes  

    def post_order(self) -> list:
        # todo
        return self._post_order(0)
      
    def _post_order(self, u) -> list:
        nodes = []
        if left(u) < self.size() and self.a[left(u)] != None:
            nodes.extend(self._post_order(left(u)))
        if right(u) < self.size() and self.a[right(u)] != None:
            nodes.extend(self._post_order(right(u)))
        nodes.append(self.a[u])
        return nodes

    def pre_order(self) -> list:
        return self._pre_order(0)
  
    def _pre_order(self, u) -> list:
        # todo
        nodes = []
        nodes.append(self.a[u])
        if left(u) < self.size() and self.a[left(u)] != None:
            nodes.extend(self._pre_order(left(u)))
        if right(u) < self.size() and self.a[right(u)] != None:
            nodes.extend(self._pre_order(right(u)))
        return nodes
      
    def size(self) -> int:
        return self.n

    def find_min(self):
        if self.n == 0: raise IndexError()
        return self.a[0]

    def _bubble_up_last(self):
        # todo
        i = self.n - 1
        while i > 0:
            p_i = parent(i)
            if self.a[i] < self.a[p_i]:
                self.a[i], self.a[p_i] = self.a[p_i], self.a[i]
                i = p_i
                p_i = parent(i)
            else:
              break
      
    def _resize(self):
        # todo
        s = _new_array(max(1,2*self.n))
        s[:self.n] = self.a[:self.n]
        self.a = s

    def _trickle_down_root(self):
        # todo
        i = 0
        l_i = left(i)
        r_i = right(i)
        while (i < self.n and (l_i < self.n or r_i < self.n)) and (self.a[i] > self.a[l_i] or self.a[i] > self.a[r_i]):
            mins = min(self.a[i], self.a[l_i], self.a[r_i])
            if mins == self.a[l_i]:
                min_i = l_i
            elif mins == self.a[r_i]:
                min_i = r_i
            else: 
                min_i = i
            self.a[i], self.a[min_i] = self.a[min_i], self.a[i]
            i = min_i
            l_i = left(i)
            r_i = right(i)

    def __str__(self):
        return str(self.a[0:self.n])

