from Interfaces import Stack
import numpy as np

class SLLStack(Stack):
  class Node:
    def __init__(self, x: object):
      self.next = None
      self.x = x

  def __init__(self):
    self.head = None
    self.tail = None
    self.n = 0

  def push(self, x: object):
    # todo
    self.u = self.Node(x)
    self.u.next = self.head
    self.head = self.u
    if self.n == 0:
      self.tail = self.u
    self.n += 1
    return x

  def pop(self) -> object:
    # todo
    if self.n == 0:
      raise IndexError()
    self.x = self.head.x
    self.head = self.head.next
    self.n -= 1
    if self.n == 0:
      self.tail = None
    return self.x

  def size(self) -> int:
    return self.n

  def __str__(self):
    s = "["
    u = self.head
    while u is not None:
      s += "%r" % u.x
      u = u.next
      if u is not None:
        s += ","
    return s + "]"

  def __iter__(self):
    self.iterator = self.head
    return self

  def __next__(self):
    if self.iterator != None:
      x = self.iterator.x
      self.iterator = self.iterator.next
    else:
      raise StopIteration()
    return x
