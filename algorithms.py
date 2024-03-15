"""Implementations of some searching and sorting algorithms"""

import random
from Interfaces import List

def linear_search(a: List, x):
  for i in range(len(a)-1):
      if a[i] == x:
          return i
  return None

def binary_search(a: List, x):
  l = 0
  r = len(a) - 1
  while l <= r:
      m = (l + r) // 2
      if x == a[m]:
          return m
      if x < a[m]:
          for i in range(l, m-1):
              if a[i] == x:
                return i
          r = m - 1
      else:
          for i in range(m+1, r):
              if a[i] == x:
                  return i
          l = m + 1
  return None
  pass

def _merge(a0: List, a1: List, a: List):
  i0 = 0
  i1 = 0
  for i in range(len(a)):
      if i0 == len(a0):
          a[i] = a1[i1]
          i1 += 1
      elif i1 == len(a1):
          a[i] = a0[i0]
          i0 += 1
      elif a0[i0] <= a1[i1]:
          a[i] = a0[i0]
          i0 += 1
      else:
          a[i] = a1[i1]
          i1 += 1
        
def merge_sort(a: List):
  if len(a) <= 1:
      return a
  m = len(a) // 2
  a0 = a[0:m]
  a1 = a[m:len(a)]
  merge_sort(a0)
  merge_sort(a1)
  return _merge(a0,a1,a)

def _quick_sort_f(a: List, start, end):
  if start < end:
      p = _partition(a, start, end)
      _quick_sort_f(a, start, p-1)
      _quick_sort_f(a, p+1, end)

def _quick_sort_r(a: List, start, end):
  if start < end:
      p = _partition(a, start, end)
      _quick_sort_r(a, start, p-1)
      _quick_sort_r(a, p+1, end)

def _partition(a ,start, end):
  pivot = a[end]
  i = start-1
  for k in range(start, end):
      if a[k] <= pivot:
          i += 1
          a[i], a[k] = a[k], a[i]
  a[i+1], a[end] = a[end], a[i+1]
  return i+1

def quick_sort(a: List, p=True):
  """
    sorts an ArrayList a using the quick sort algorithm.
    If parameter p is True, the quick sort algorithm uses a randomly chosen element from a as pivot.
    Otherwise, the quick sort algorithm uses the first element as pivot.
    """
  if p:
    _quick_sort_r(a, 0, a.size() - 1)
  else:
    _quick_sort_f(a, 0, a.size() - 1)
