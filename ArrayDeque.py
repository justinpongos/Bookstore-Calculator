from Interfaces import Deque
from ArrayList import ArrayList


class ArrayDeque(Deque, ArrayList):
  """
  ArrayDeque: Implementation of a Deque interface using ArrayBase list. 
  It inheritances from an ArrayList
  """

  def __init__(self):
    """
    Initialization of the base class ArrayList
    """
    ArrayList.__init__(self)

  def add_first(self, x: object):
    """
    inserts x in the head of the deque.
    """
    self.add(0, x)

  def add_last(self, x: object):
    """    
    inserts x in the tail of the deque.
    """
    self.add(self.n, x)

  def remove_first(self) -> object:
    """
    removes from the head of the  deque.
    """
    return self.remove(0)

  def remove_last(self) -> object:
    """removes from the tail of the  deque."""
    return self.remove(self.n - 1)