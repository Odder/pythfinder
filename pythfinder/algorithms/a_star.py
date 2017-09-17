# -*- coding: utf-8 -*-

from graphs.PriorityQueue import PriorityQueue
import heuristics

def a_star(graph, start, goal, heuristic = heuristics.manhattan, bidirectional = False):
  '''
  a* algorithm
  '''

  # Initialise priority queue
  queue = PriorityQueue()
  queue.append(start, 0)

  # Initialise trailing
  cameFrom = {
    start: 0
  }
  # Initialise weights of all nodes
  costs = {
    start: 0
  }

  if bidirectional:
    # Initialise priority queue
    queue2 = PriorityQueue()
    queue2.append(goal, 0)

    # Initialise trailing
    cameFrom2 = {
      goal: 0
    }
    # Initialise weights of all nodes
    costs2 = {
      goal: 0
    }    

  # Statistics
  nodesVisited = 0
 
  # As long as there are nodes to visit, let's visit!
  while not queue.empty():

    # Get the next item from the queue
    current = queue.pop()

    nodesVisited += 1
 
    # We are done!
    if not bidirectional and current == goal \
      or bidirectional and current in costs2:


      if bidirectional:
        totalCost = costs[current] + costs2[current]
      else:
        totalCost = costs[goal]


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
        "length": totalCost,
        "nodesVisited": nodesVisited
      }
 
    # Append all neighbouring nodes to the queue
    for (next, cost) in graph.neighbours(current):

      # Apply cost to new node (grid -> +1)
      newCost = costs[current] + cost

      # If node is not already in the queue, or the current registered cost is 
      # higher, we need to set/update the cost for that node
      if next not in costs or newCost < costs[next]:

        # Update cost
        costs[next] = newCost

        # Add heuristics
        priority = newCost + heuristic(goal, next)

        # Append to queue
        queue.append(next, priority)

        # Append to trail
        cameFrom[next] = current
    
    if bidirectional:   
      # Get the next item from the queue
      current = queue2.pop()

      nodesVisited += 1

      # Append all neighbouring nodes to the queue
      for (next, cost) in graph.neighbours(current):

        # Apply cost to new node (grid -> +1)
        newCost = costs2[current] + cost

        # If node is not already in the queue, or the current registered cost is 
        # higher, we need to set/update the cost for that node
        if next not in costs2 or newCost < costs2[next]:

          # Update cost
          costs2[next] = newCost

          # Add heuristics
          priority = newCost + heuristic(start, next)

          # Append to queue
          queue2.append(next, priority)

          # Append to trail
          cameFrom2[next] = current
 
  # We only reach this part if no path was found
  raise Exception('no path found')