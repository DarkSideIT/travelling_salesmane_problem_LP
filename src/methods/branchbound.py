import numpy as np
from tkinter import *

def tsp_branch_and_bound(graph):
    n = len(graph)
    min_cost = np.inf
    best_path = None

    def branch_and_bound(path, cost):
        nonlocal min_cost, best_path

        if len(path) == n:
            cost += graph[path[-1]][path[0]]  # Complete the cycle
            if cost < min_cost:
                min_cost = cost
                best_path = path[:]
            return

        for i in range(n):
            if i not in path:
                new_path = path[:]
                new_path.append(i)

                new_cost = cost + graph[path[-1]][i]

                if new_cost < min_cost:
                    branch_and_bound(new_path, new_cost)

    start_node = 0
    initial_path = [start_node]
    branch_and_bound(initial_path, 0)
    for i in range(len(best_path)):
        best_path[i] += 1
    best_path.append(1)
    
    return best_path, min_cost






