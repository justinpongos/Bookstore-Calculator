import numpy as np
from Interfaces import List


class ArrayList(List):
  def __init__(self):
    self.n = 0
    self.j = 0
    self.a = self.new_array(1)

  def new_array(self, n: int) -> np.array:
    return np.zeros(n, object)

  def resize(self):
    self.b = self.new_array(max(1,2 * self.n))
    for self.k in range(self.n):
      self.b[self.k] = self.a[(self.j + self.k) % len(self.a)]
    self.a = self.b
    self.j = 0
    pass

  def get(self, i: int) -> object:
    if i < 0 or i >= self.n:
      raise IndexError()
    return self.a[(self.j + i) % len(self.a)]
    ##returns the element at position i
        ##Inputs:
            ##i: Index that is integer non negative and at most n

  def set(self, i: int, x: object) -> object:
    if i < 0 or i >= self.n:
      raise IndexError()
    self.a[(self.j + i) % len(self.a)] = x
    
    ##sets the value x at the index i.
        ##Inputs:
            ##i: Index that is integer non negative and at most n
            ##x: Object type, i.e., any object
    pass

  def append(self, x: object):
    self.add(self.n, x)

  def add(self, i: int, x: object):
    if i < 0 or i > self.n:
      raise IndexError()
    if len(self.a) == self.n: 
      self.resize()
    if i < self.n/2:
      for k in range(0, i):
        self.a[(self.j + k - 1) % len(self.a)] = self.a[(self.j + k) % len(self.a)]
      self.j = (self.j - 1) % len(self.a)
    else:
      for k in range(self.n-1, i-1, -1):
        self.a[(self.j + k + 1) % len(self.a)] = self.a[(self.j + k) % len(self.a)]
    self.a[(self.j + i) % len(self.a)] = x
    self.n += 1
    
    ##inserts value x at position i of the list and increment the number of elements 
    ##in the list.
      ##Inputs:
          ##i: Index that is integer non negative and at most n
          ##x: Object type, i.e., any object

  def remove(self, i: int) -> object:
    if i < 0 or i >= self.n:
      raise IndexError()
    x = self.a[(self.j+i) % len(self.a)]
    if i < self.n/2:
      for k in range(i, 0 , -1):
        self.a[(self.j + k) % len(self.a)] = self.a[(self.j + k - 1) % len(self.a)]
      self.j = (self.j + 1) % len(self.a)
    else:
      for k in range(i, self.n-1):
        self.a[(self.j + k) % len(self.a)] = self.a[(self.j + k + 1) % len(self.a)]
    self.n -= 1
    if len(self.a) > 3*self.n: 
      self.resize()
    return x
    
    ##removes the value at index i and returns it, if it exists.
      ##Inputs:
        ##i: index that is integer non negative at most n - 1


  def size(self) -> int:
    return self.n

  def __str__(self):
    s = "["
    for i in range(0, self.n):
      s += "%r" % self.a[(i + self.j) % len(self.a)]
      if i < self.n - 1:
        s += ","
    return s + "]"

  def __iter__(self):
    self.iterator = 0
    return self

  def __next__(self):
    if self.iterator < self.n:
      x = self.a[(self.iterator + self.j) % len(self.a)]
      self.iterator += 1
    else:
      raise StopIteration()
    return x
