import heapq

def heap_dijkstra(graph, start):
    """
    Implements Dijkstra's algorithm to find the shortest path from the start node to all other nodes in a weighted graph.
    
    Parameters:
    - graph (list of lists of tuples): Adjacency matrix where each element graph[u][v] is a tuple (weight, destination).
    - start (int): The starting node for the algorithm.

    Returns:
    - dist (list): The shortest distance from the start node to each node.
    - prev (list): The previous node in the optimal path from the start node for each node.
    """

    # Number of nodes in the graph
    num_nodes = len(graph)
    
    # Distance table initialized to infinity for all nodes except the start node
    dist = [float('inf')] * num_nodes
    dist[start] = 0
    
    # Previous node table to reconstruct the shortest path
    prev = [None] * num_nodes
    
    # Priority queue to select the node with the smallest distance; initialized with the start node
    priority_queue = [(0, start)]  # (distance, node)
    
    # Set of visited nodes to avoid processing a node more than once
    visited = set()
    
    while priority_queue:
        # Get the node with the smallest distance
        current_dist, u = heapq.heappop(priority_queue)
        
        # If this node has already been visited, skip it
        if u in visited:
            continue
        
        # Mark this node as visited
        visited.add(u)
        
        # Iterate over neighboring nodes
        for weight, v in graph[u]:
            # Calculate the new distance to the neighboring node
            distance = current_dist + weight
            
            # If the new distance is smaller, update it and push to priority queue
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
    - graph (list of lists of tuples): Adjacency matrix where each element graph[u][v] is a tuple (weight, destination).
    - start (int): The starting node for the algorithm.

    Returns:
    - dist (list): The shortest distance from the start node to each node.
    - prev (list): The previous node in the optimal path from the start node for each node.
    """

    # Number of nodes in the graph
    num_nodes = len(graph)
    
    # Distance table initialized to infinity for all nodes except the start node
    dist = [float('inf')] * num_nodes
    dist[start] = 0
    
    # Previous node table to reconstruct the shortest path
    prev = [None] * num_nodes
    
    # List of nodes to be processed
    unvisited = list(range(num_nodes))
    
    while unvisited:
        # Find the node with the smallest distance in the unvisited list
        u = min(unvisited, key=lambda node: dist[node])
        
        # Remove the node from the unvisited list
        unvisited.remove(u)
        
        # Iterate over neighboring nodes
        for weight, v in graph[u]:
            # Calculate the new distance to the neighboring node
            distance = dist[u] + weight
            
            # If the new distance is smaller, update it and set the previous node
            if distance < dist[v]:
                dist[v] = distance
                prev[v] = u
    
    return dist, prev

# Example usage:
# Graph representation as an adjacency matrix:
# graph[u] = [(weight, v), (weight, w), ...] where 'weight' is the weight of the edge from node 'u' to node 'v'
graph = [
    [(1, 1), (4, 2)],
    [(1, 0), (2, 2), (6, 3)],
    [(4, 0), (2, 1), (3, 3)],
    [(6, 1), (3, 2)]
]

start_node = 0
distances, predecessors = dijkstra_no_heap(graph, start_node)

print("Distances from start node:", distances)
print("Predecessors in the shortest path:", predecessors)
print('-'*20)
distances, predecessors = heap_dijkstra(graph, start_node)

print("Distances from start node:", distances)
print("Predecessors in the shortest path:", predecessors)
