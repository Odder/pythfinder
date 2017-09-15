# -*- coding: utf-8 -*-

import heapq
 
class PriorityQueue:
  '''
 Simple PriorityQueue class using the heapq library
 '''
  def __init__(self):
    self.elements = []
 
  def empty(self):
    return len(self.elements) == 0
 
  def append(self, node, priority):
    heapq.heappush(self.elements, (priority, node))
 
  def pop(self):
    return heapq.heappop(self.elements)[1]