import heapq

def dijkstra(n, graph, start):
    distances = [float('inf')] * n
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))

# Dijkstra from city 0
dist_from_start = dijkstra(n, graph, 0)

# Dijkstra from city N-1
dist_from_end = dijkstra(n, graph, n - 1)

max_time = 0
for i in range(n):
    max_time = max(max_time, dist_from_start[i] + dist_from_end[i])

print(max_time)
