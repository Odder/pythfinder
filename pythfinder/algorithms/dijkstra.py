# -*- coding: utf-8 -*-

from algorithms.a_star import a_star
 
def dijkstra(graph, start, goal, bidirectional = False):
  '''
  just do a* without heuristics
  '''
  return a_star(graph, start, goal, lambda _,__: 0, bidirectional = bidirectional)