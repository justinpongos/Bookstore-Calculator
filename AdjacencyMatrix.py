from Interfaces import Graph, List
import ArrayList
import ArrayQueue
import ArrayStack
import numpy as np

"""An implementation of the adjacency list representation of a graph"""
class AdjacencyMatrix(Graph):

  def __init__(self, n: int):
    self.n = n
    self.adj = np.zeros((self.n, self.n), dtype=int)

  def add_edge(self, i: int, j: int):
    # todo
      if i < 0 or j < 0 or i >= self.n or j >= self.n:
          raise IndexError()
      self.adj[i][j] = True

  def remove_edge(self, i: int, j: int):
    # todo
      if i < 0 or j < 0 or i >= self.n or j >= self.n:
          raise IndexError()
      if not self.has_edge(i, j):
          return False
      self.adj[i][j] = False
      return True

  def has_edge(self, i: int, j: int) -> bool:
    # todo
      if i < 0 or j < 0 or i >= self.n or j >= self.n:
          raise IndexError()
      return self.adj[i][j]

  def out_edges(self, i) -> List:
    # todo
      if i < 0 or i >= self.n:
          raise IndexError()
      out = []
      for j in range(self.n):
          if self.has_edge(i,j):
              out.append(j)
      return out
  
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
          for u in range(self.n):
              if self.has_edge(current, u):
                  j.append(u)
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
          for u in range(self.n):
              if self.has_edge(current, u):
                  j.append(u)
          for k in range(len(j) -1, -1, -1):
              if seen[j[k]] == False:
                  s.push(j[k])
      return vert

  def __str__(self):
    s = ""
    for i in range(0, self.n):
      s += "%i:  %r\n" % (i, self.adj[i].__str__())
    return s
