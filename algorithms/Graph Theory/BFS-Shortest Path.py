import time
from graph_representation.visualize import showgraph, showpath

graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G', 'H'],
    'D': ['I', 'J'],
    'E': ['K'],
    'F': ['K', 'L'],
    'G': ['L', 'M'],
    'H': ['M'],
    'I': ['N'],
    'J': ['N', 'O'],
    'K': ['P'],
    'L': ['P'],
    'M': ['P'],
    'N': ['P'],
    'O': ['P'],
    'P': []
}


def graph_bfs_shortest_path(graph, starting_node, ending_node): # this is a BFS with a GRAPH - > implmented using a dictonary to show vertices and edges
    visited = set()
    queue = [(starting_node, [starting_node])]
    visited.add(starting_node) # add starting node to visited set

    while queue: #loop untill the queue is empty
        current_node, path = queue.pop(0) # remove the first element from the queue - > using the first in first out principle
        print(current_node)
        for neighbour in graph[current_node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, path+[neighbour]))
    return (' -> '.join(path), path)

start_time = time.time()
shortest_path = graph_bfs_shortest_path(graph, 'A', 'P')
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time for Graph BFS: {execution_time} seconds \n---------------\n")
print(f"Shortest path from 'A' to 'P': \n{shortest_path[0]}")
showpath(graph, shortest_path[1])
