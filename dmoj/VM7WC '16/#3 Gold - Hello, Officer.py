import heapq

def dijkstra(n, graph, start):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]  # (distance, node)
    
    while pq:
        current_dist, node = heapq.heappop(pq)
        
        if current_dist > dist[node]:
            continue
        
        for neighbor, weight in graph[node]:
            distance = current_dist + weight
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return dist

n, m, b, q = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
    graph[y].append((x, z))

distances = dijkstra(n, graph, b)

for _ in range(q):
    a = int(input())
    if distances[a] == float('inf'):
        print(-1)
    else:
        print(distances[a])