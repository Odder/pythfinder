import random
import pprint
from pythfinder.graphs.Graph import Graph
from pythfinder.algorithms.BFS import BFS


G = Graph()

for i in range(30):
  for j in range(i,30):
    dice = random.randint(0,100)
    weight = random.randint(1000,1050)
    if dice % 4:
      G.addEdge((i,j),(i+1,j), True, weight)
    weight = random.randint(1,11)
    if dice % 3:
      G.addEdge((i,j),(i,j+1), True, weight)
#G.addEdge((2,4), (2,3))
solutions = {
  'BFS': BFS(G, (9,9), (19,19))
}
for alg in solutions:
  print(alg, '\n    Cost -> ', solutions[alg]['length'],'\n    Nodes visited -> ',solutions[alg]['nodesVisited'],'\n    Route -> ', solutions[alg]['route'])