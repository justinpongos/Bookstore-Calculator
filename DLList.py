from Interfaces import List
import numpy as np

class DLList(List):
  class Node:
    def __init__(self, x: object):
      self.next = None
      self.prev = None
      self.x = x

  def __init__(self):
    self.dummy = DLList.Node("")
    self.dummy.next = self.dummy
    self.dummy.prev = self.dummy
    self.n = 0

  def get_node(self, i: int) -> Node:
    # todo
    if i < 0 or i >= self.n:
      return self.dummy
    if i < self.n/2:
      self.p = self.dummy.next
      for k in range(i):
        self.p = self.p.next
    else:
      self.p = self.dummy
      for k in range(self.n - i):
        self.p = self.p.prev
    return self.p

  def get(self, i) -> object:
    # todo
    if i < 0 or i >= self.n:
      raise IndexError()
    return self.get_node(i).x

  def set(self, i: int, x: object) -> object:
    # todo
    if i < 0 or i >= self.n:
      raise IndexError()
    self.u = self.get.node(i)
    self.y = self.u.x
    self.u.x = self.x
    return self.y

  def add_before(self, w: Node, x: object) -> Node:
    # todo
    if w == None:
      raise IndexError()
    self.u = self.Node(x)
    self.u.prev = w.prev
    self.u.next = w
    w.prev = self.u
    self.u.prev.next = self.u
    self.n += 1
    return self.u

  def add(self, i: int, x: object):
    # todo
    if i < 0 or i > self.n:
      raise IndexError()
    return self.add_before(self.get_node(i), x)

  def _remove(self, w: Node):
    # todo
    ##w = self.get_node(self.i)
    if self.n == 0:
      raise IndexError()
    w.prev.next = w.next
    w.next.prev = w.prev
    self.n -= 1
    return w.x

  def remove(self, i: int):
    if i < 0 or i > self.n: raise IndexError()
    return self._remove(self.get_node(i))

  def size(self) -> int:
    return self.n

  def append(self, x: object):
    self.add(self.n, x)

  def isPalindrome(self) -> bool:
    # todo
    if self.n <= 1:
      return True
    head = self.get(0)
    tail = self.get(self.n-1)
    for i in range(self.n // 2):
      if str(self.get(i)).isalnum():
        head = self.get(i)
      if str(self.get(self.n -1 -i)).isalnum():
        tail = self.get(self.n-1 -i)
      if str(head).lower() != str(tail).lower():
        return False
      ##if str(self.get(self.n(i))) != self.get((self.n -1 -i)):
    return True
     
  def reverse(self):
    # todo
    n = self.dummy.next
    while n != self.dummy:
      n.prev, n.next = n.next, n.prev
      n = n.prev
    self.dummy.prev, self.dummy.next = self.dummy.next, self.dummy.prev

  def __str__(self):
    s = "["
    u = self.dummy.next
    while u is not self.dummy:
      s += "%r" % u.x
      u = u.next
      if u is not None:
        s += ","
    return s + "]"

  def __iter__(self):
    self.iterator = self.dummy.next
    return self

  def __next__(self):
    if self.iterator != self.dummy:
      x = self.iterator.x
      self.iterator = self.iterator.next
    else:
      raise StopIteration()
    return x
