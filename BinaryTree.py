import SLLQueue
from Interfaces import Tree


class BinaryTree(Tree):
    class Node:
        def __init__(self, key: object = None, val: object = None):
            self.parent = self.left = self.right = None
            self.k = key
            self.v = val

        def set_key(self, x):
            self.k = x

        def set_val(self, v):
            self.v = v

        def insert_left(self, u):
            self.left = u
            self.left.parent = self
            return self.left

        def insert_right(self, u):
            self.right = u
            self.right.parent = self
            return self.right

        def __str__(self):
            return f"({self.k}, {self.v})"

    def __init__(self):
        self.r = None

    def depth(self, u: Node) -> int:
        # todo
        if u == None:
          return -1
        self.d = 0
        self.current_node = u
        while self.current_node != self.r:
          self.current_node = self.current_node.parent
          self.d += 1
        return self.d

    def height(self) -> int:
        return self._height(self.r)

    def _height(self, u: Node) -> int:
        # todo
        if u == None:
          return -1
        return 1 + max(self._height(u.left), self._height(u.right))

    def size(self) -> int:
        return self._size(self.r)

    def _size(self, u: Node) -> int:
        # todo
        if u == None:
          return 0
        return 1 + self._size(u.left) + self._size(u.right)

    def bf_order(self):
        # todo
        self.nodes = []
        self.q = SLLQueue.SLLQueue()
        if self.r != None:
          self.q.add(self.r)
        while self.q.size() > 0:
          self.u = self.q.remove()
          self.nodes.append(self.u)
          if self.u.left != None:
            self.q.add(self.u.left)
          if self.u.right != None:
            self.q.add(self.u.right)
        return self.nodes

    def in_order(self) -> list:
        return self._in_order(self.r)

    def _in_order(self, u: Node) -> list:
        # todo
        nodes = []
        if u.left != None:
          nodes.extend(self._in_order(u.left))
        nodes.append(u)
        if u.right != None:
          nodes.extend(self._in_order(u.right))
        return nodes  

    def post_order(self) -> list:
        return self._post_order(self.r)

    def _post_order(self, u: Node):
        # todo
        nodes = []
        if u.left != None:
          nodes.extend(self._post_order(u.left))
        if u.right != None:
          nodes.extend(self._post_order(u.right))
        nodes.append(u)
        return nodes

    def pre_order(self) -> list:
        return self._pre_order(self.r)

    def _pre_order(self, u: Node):
        # todo
        nodes = []
        nodes.append(u)
        if u.left != None:
          nodes.extend(self._pre_order(u.left))
        if u.right != None:
          nodes.extend(self._pre_order(u.right))
        return nodes

    def __str__(self):
        nodes = self.bf_order()
        nodes_str = [str(node) for node in nodes]
        return ', '.join(nodes_str)