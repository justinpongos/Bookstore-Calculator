"""An implementation of the adjacency list representation of a graph"""
from Interfaces import Graph, List
import numpy as np
import copy
import ArrayList
import ArrayStack
import ArrayQueue


class AdjacencyList(Graph):

  def __init__(self, n: int):
    self.n = n
    self.adj = np.zeros(n, dtype=ArrayList.ArrayList)
    for i in range(self.n):
      self.adj[i] = ArrayList.ArrayList()

  def add_edge(self, i: int, j: int):
    # todo
      if i < 0 or j < 0 or i >= self.n or j >= self.n:
          raise IndexError()
      if not self.has_edge(i,j):
          self.adj[i].append(j)

  def remove_edge(self, i: int, j: int):
    # todo
      if i < 0 or j < 0 or i >= self.n or j >= self.n:
          raise IndexError()
      for k in range(self.adj[i].size()):
          if self.adj[i].get(k) == j:
              self.adj[i].remove(k)
              return True
      return False

  def has_edge(self, i: int, j: int) -> bool:
    # todo
      if i < 0 or j < 0 or i >= self.n or j >= self.n:
          raise IndexError()
      for k in range(self.adj[i].size()):
          if self.adj[i].get(k) == j:
              return True
      return False

  def out_edges(self, i) -> List:
    # todo
      return self.adj[i]
    
  def in_edges(self, j) -> List:
    # todo
      if j < 0 or j >= self.n:
          raise IndexError()
      temp = []
      for i in range(self.n):
          if self.has_edge(i,j):
              temp.append(i)
      return temp

  def size(self):
    return self.n
    
  def bfs(self, i: int):
    # todo
      vert = []
      seen = [False]*self.n
      q = ArrayQueue.ArrayQueue()
      q.add(i)
      vert.append(i)
      seen[i] = True
      while q.n > 0:
          current = q.remove()
          j = []
          j.extend(self.adj[current])
          for k in j:
              if seen[k] == False:
                  q.add(k)
                  vert.append(k)
                  seen[k] = True
      return vert

  def dfs(self, i: int):
    # todo
      vert = []
      s = ArrayStack.ArrayStack()
      seen = [False]*self.n
      s.push(i)
      while s.n > 0:
          current = s.pop()
          if seen[current] == False:
              vert.append(current)
              seen[current] = True
          j = []
          j.extend(self.adj[current])
          for k in range(len(j) -1, -1, -1):
              if seen[j[k]] == False:
                  s.push(j[k])
      return vert

  def __str__(self):
    s = ""
    for i in range(0, self.n):
      s += "%i:  %r\n" % (i, self.adj[i].__str__())
    return s

  def __str__(self):
    s = ""
    for i in range(0, self.n):
      s += "%i,%r\n" % (i, self.adj[i].__str__())
    return s
