import numpy as np
from Interfaces import Stack
from Interfaces import List

class ArrayStack(Stack, List):
  def __init__(self):
    self.a = self.new_array(1)
    self.n = 0

  def new_array(self, n: int) -> np.array:
    return np.zeros(n, object)

  def resize(self):
    self.b = self.new_array(max(1,2*self.n))
    for k in range(self.n):
      self.b[k] = self.a[k]
    self.a = self.b
          ## Resize the array
    pass

  def get(self, i: int) -> object:
    if 0 <= i < self.n:
      return self.a[i]

  def set(self, i: int, x: object) -> object:
    if 0 <= i < self.n:
      raise IndexError()
    self.y = self.a[i]
    self.a[i] = x
    return self.y

  def add(self, i: int, x: object):
    if i < 0 or i > self.n:
      raise IndexError()
    if len(self.a) == self.n:
      self.resize()
    for k in range(self.n-1, i-1, -1):
      self.a[k] = self.a[k-1]
    self.a[i] = x
    self.n += 1
    ##shift all j > i one position to the right and add element x in position i
    pass

  def remove(self, i: int) -> object:
    if i < 0 or i >= self.n:
      raise IndexError()
    self.y = self.a[i]
    for k in range(i, self.n - 1):
      self.a[k] = self.a[k + 1]
    self.n -= 1
    if len(self.a) > 3*self.n-1:
      self.resize()
    ##remove element i and shift all j > i one position to the left
    return self.y

  def push(self, x: object):
    self.add(self.n, x)

  def pop(self) -> object:
    return self.remove(self.n - 1)

  def size(self):
    ##size: Returns the size of the stack Return: an integer greater or equal to zero representing the number of elements in the stack
    return self.n

  def __str__(self) -> str:
    ##__str__: Returns the content of the string using print(s) where s is an instance of the ArrayStack Return: String with the content of the stack
    s = "["
    for i in range(0, self.n):
      s += "%r" % self.a[i]
      if i < self.n - 1:
        s += ","
    return s + "]"

  def __iter__(self):
    ##Initialize the iterator. It is to be use in for loop
    self.iterator = 0
    return self

  def __next__(self):
    ##Move to the next item. It is to be use in for loop
    if self.iterator < self.n:
      x = self.a[self.iterator]
      self.iterator += 1
    else:
      raise StopIteration()
    return x
