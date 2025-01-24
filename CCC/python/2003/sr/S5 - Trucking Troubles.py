import heapq

c, r, d = map(int, input().split())
graph = [[] for _ in range(c + 1)]

for _ in range(r):
    x, y, w = map(int, input().split())
    graph[x].append((y, w))
    graph[y].append((x, w))

# Read the destination cities
destinations = [int(input()) for _ in range(d)]

# Initialize max_min_weight array and priority queue
max_min_weight = [-1] * (c + 1)
max_min_weight[1] = float('inf')
priority_queue = []
heapq.heappush(priority_queue, (-float('inf'), 1))  # Start from city 1 with the maximum possible weight

# Dijkstra's algorithm using a heap (priority queue)
while priority_queue:
    current_weight, current_city = heapq.heappop(priority_queue)
    current_weight = -current_weight  # Convert back to positive weight
    
    for neighbor, weight in graph[current_city]:
        min_weight_on_path = min(current_weight, weight)
        if min_weight_on_path > max_min_weight[neighbor]:
            max_min_weight[neighbor] = min_weight_on_path
            heapq.heappush(priority_queue, (-min_weight_on_path, neighbor))

# Find the minimum weight across all destination cities
result = float('inf')
for destination in destinations:
    result = min(result, max_min_weight[destination])

print(result)