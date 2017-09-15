# -*- coding: utf-8 -*-

from collections import deque

def BFS(graph, start, goal):

  # Initialise priority queue
  queue = deque()
  queue.append(start)

  # Initialise trailing
  cameFrom = {
    start: 0
  }
  # Initialise weights of all nodes
  costs = {
    start: 0
  }

  # Statistics
  nodesVisited = 0

  # As long as there are nodes to visit, let's visit!
  while queue:

    # Get the next item from the queue
    current = queue.popleft()

    nodesVisited += 1
 
    # We are done!
    if current == goal:

      # Backtrack the route for output
      route = []
      while current:
        route.append(current)
        current = cameFrom[current]

      # Reverse the route 
      route = route[::-1]

      # Return a nice object with the route and length 
      return {
        "route": route,
        "length": costs[goal],
        "nodesVisited": nodesVisited
      }
 
    # Append all neighbouring nodes to the queue
    for (next, cost) in graph.neighbours(current):

      # Apply cost to new node (grid -> +1)
      newCost = costs[current] + cost

      # If node is not already in the queue we need to append it
      if next not in costs:

        # Update cost
        costs[next] = newCost

        # Append to queue
        queue.append(next)

        # Append to trail
        cameFrom[next] = current
 
  # We only reach this part if no path was found
  raise Exception('no path found')