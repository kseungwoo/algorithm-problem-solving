""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
from collections import deque
import sys


def check_binary_search_tree_(root):
    q = deque([(root, float('-inf'), float('inf'))])
    while q:
        cur, floor, ceil = q.popleft()
        if cur.left is not None:
            if cur.left.data >= cur.data or cur.left.data <= floor:
                return False
            else:
                q.append((cur.left, floor, min(ceil, cur.data)))
        if cur.right is not None:
            if cur.right.data <= cur.data or cur.right.data >= ceil:
                return False
            else:
                q.append((cur.right, max(floor, cur.data), ceil))
    return True
