import numpy as np
from ArrayStack import ArrayStack
import BinaryTree
import re
import ChainedHashTable
import DLList
import operator


class Calculator:
  def __init__(self):
    self.dict = ChainedHashTable.ChainedHashTable(DLList.DLList)
  def set_variable(self, k: str, v: float):
    self.dict.add(k, v)
    
  def matched_expression(self, s: str) -> bool:
    stack = ArrayStack()
    for k in range(len(s)):
      if s[k] == "(":
        stack.push(s[k])
      if s[k] == ")" and len(stack) == 0:
        return False
      if s[k] == ")" and len(stack) != 0:
        stack.pop()
    if len(stack) == 0:
      return True
    # take string and check if paranthesis are valid, use arraystack
  
  def print_expression(self, exp):
    variables = [x for x in re.split('\W+', exp) if x.isalnum()]
    everything_else = re.split('\w+', exp)
    exp = ""
    for i in range(len(variables)):
      if self.dict.find(variables[i]) != None:
        variables[i] = self.dict.find(variables[i])
    for k in range(len(variables) + len(everything_else)):
      if k < len(everything_else):
        exp += str(everything_else[k])
      if k < len(variables):
        exp += str(variables[k])
    return exp
    
  def _build_parse_tree(self, exp: str) -> str:
      if self.matched_expression(exp) is False:
        raise IndexError()

      tokens = []
      i = 0
      while i < len(exp):
          current_token = ""
          if not exp[i].isalnum():
              current_token = exp[i]
              tokens.append(current_token)
              i += 1
              continue
          while exp[i].isalnum() is True:
              current_token += exp[i]
              i += 1
          tokens.append(current_token)  

      t = BinaryTree.BinaryTree()
      t.r = t.Node()
      current = t.r
      
      for token in tokens:
          nd = t.Node()
          if token == '(':
              current.insert_left(nd)
              current = current.left
          if token == '+' or token == '-' or token == '/' or token == '*':
              current.set_val(token)
              current.set_key(token)
              current.insert_right(nd)
              current = current.right
          if token.isalnum():
              current.set_key(token)
              current.set_val(self.dict.find(token))
              current = current.parent
          if token == ')':
              current = current.parent
      return t

  def _evaluate(self, u):
    op = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    #todo
    if u.left is not None and u.right is not None:
      fn = op[u.k]
      return fn(self._evaluate(u.left), self._evaluate(u.right))
    elif u.left is None and u.right is None:
      if u.v is not None:
        return float(u.v)
      raise ValueError(f"Missing value for variable {u.k}")
    elif u.left is not None:
      return self._evaluate(u.left)
    else:
      return self._evaluate(u.right)
      
  def evaluate(self, exp):
    parseTree = self._build_parse_tree(exp)
    return self._evaluate(parseTree.r)
