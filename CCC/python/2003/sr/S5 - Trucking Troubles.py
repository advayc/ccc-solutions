'''total_cities, roads, dest_cities = map(int, input().split())
graph = {}
for i in range(roads):
    '''

c, r, d = map(int, input().split())
graph = [[] for _ in range(c + 1)]
for _ in range(r):
    x, y, w = map(int, input().split())
    graph[x].append((y, w))
    graph[y].append((x, w))

# Read the destination cities
destinations = [int(input()) for _ in range(d)]

# Initialize the maximum minimum weight array and the queue for BFS
max_min_weight = [-1] * (c + 1)
max_min_weight[1] = float('inf')  # Starting city with maximum possible weight

# Initialize queue for BFS
queue = [1]  # Start with the starting city

# Perform BFS
while queue:
    current_city = queue.pop(0)  # Dequeue the front element
    current_weight = max_min_weight[current_city]
    
    for neighbor, weight in graph[current_city]:
        min_weight_on_path = min(current_weight, weight)
        if min_weight_on_path > max_min_weight[neighbor]:
            max_min_weight[neighbor] = min_weight_on_path
            queue.append(neighbor)  # Enqueue the neighbor

# Find the minimum weight across all destination cities
result = float('inf')
for destination in destinations:
    result = min(result, max_min_weight[destination])

print(result)
