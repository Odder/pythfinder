# -*- coding: utf-8 -*-

class Graph:
  '''
  A simple Graph implementation that only keeps track of edges.
  Nodes are implicated by inclusion in edges. And thus should be stored externally
  '''
  def __init__(self):
    self.edges = {}
    self.costs = {}
 
  def neighbours(self, id):
    return self.edges[id]
 
  def addEdge(self, id, target, bidirectional = False, weight = 1):
    if id not in self.edges:
      self.edges[id] = []
    self.edges[id].append((target, weight))

    if bidirectional:
      self.addEdge(target, id, False, weight)
 
  def removeEdge(self, id, target):
    return
    #self.edges[id].remove(target)
    #self.edges[target].remove(id)