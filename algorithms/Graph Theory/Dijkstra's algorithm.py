import heapq
from graph_representation.visualize import showweightedpath

def heap_dijkstra(graph, start):
    """
    Implements Dijkstra's algorithm to find the shortest path from the start node to all other nodes in a weighted graph.
    
    Parameters:
    - graph (dict): Adjacency list where each key is a node, and the value is a list of tuples (weight, destination).
    - start (str): The starting node for the algorithm.

    Returns:
    - dist (dict): The shortest distance from the start node to each node.
    - prev (dict): The previous node in the optimal path from the start node for each node.
    """

    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    prev = {node: None for node in graph}
    priority_queue = [(0, start)]  # (distance, node)
    visited = set()
    
    while priority_queue:
        current_dist, u = heapq.heappop(priority_queue)
        
        if u in visited:
            continue
        
        visited.add(u)
        
        for weight, v in graph[u]:
            distance = current_dist + weight
            
            if distance < dist[v]:
                dist[v] = distance
                prev[v] = u
                heapq.heappush(priority_queue, (distance, v))
    
    return dist, prev

def dijkstra_no_heap(graph, start):
    """
    Implements Dijkstra's algorithm to find the shortest path from the start node to all other nodes in a weighted graph,
    using a simple list to track the minimum distance instead of a priority queue.

    Parameters:
    - graph (dict): Adjacency list where each key is a node, and the value is a list of tuples (weight, destination).
    - start (str): The starting node for the algorithm.

    Returns:
    - dist (dict): The shortest distance from the start node to each node.
    - prev (dict): The previous node in the optimal path from the start node for each node.
    """

    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    prev = {node: None for node in graph}
    unvisited = list(graph.keys())
    
    while unvisited:
        u = min(unvisited, key=lambda node: dist[node])
        unvisited.remove(u)
        
        for weight, v in graph[u]:
            distance = dist[u] + weight
            
            if distance < dist[v]:
                dist[v] = distance
                prev[v] = u
    
    return dist, prev

def reconstruct_path(predecessors, start, end):
    """
    Reconstruct the path from the start node to the end node using the predecessors list.
    
    Parameters:
    - predecessors (dict): The dictionary of predecessors from Dijkstra's algorithm.
    - start (str): The starting node.
    - end (str): The ending node.
    
    Returns:
    - path (list): The path from start to end.
    """
    path = []
    current = end
    while current is not None:
        path.insert(0, current)
        current = predecessors[current]
    
    if path[0] == start:
        return path
    else:
        return []  # No path found

# Example usage:
graph = {
    'A': [(1, 'B'), (4, 'C')],
    'B': [(1, 'A'), (2, 'C'), (6, 'D')],
    'C': [(4, 'A'), (2, 'B'), (3, 'D')],
    'D': [(6, 'B'), (3, 'C')]
}

start_node = 'A'
end_node = 'D'

# Dijkstra without heap
distances_no_heap, predecessors_no_heap = dijkstra_no_heap(graph, start_node)
path_no_heap = reconstruct_path(predecessors_no_heap, start_node, end_node)
print("Path (no heap):", path_no_heap)
showweightedpath(graph, path_no_heap)

# Dijkstra with heap
distances_with_heap, predecessors_with_heap = heap_dijkstra(graph, start_node)
path_with_heap = reconstruct_path(predecessors_with_heap, start_node, end_node)
print("Path (with heap):", path_with_heap)
showweightedpath(graph, path_with_heap)
