import heapq
from collections import defaultdict

n=int(input())
s,e = map(int, input().split())
graph = defaultdict(list)

for _ in range(e):
    a, b, c, d = map(int, input().split())
    graph[a].append((c, b, d))  # (distance, target node, type)
    graph[b].append((c, a, d))

start, end = 0, n - 1
pq = [(0, 0, start)]  # (distance, sunlight exposure, node)
distance = {(start, 0): 0}
visited = set()

while pq:
    d1, sun, node = heapq.heappop(pq)

    if node == end:
        print(d1)
        break

    if (node, sun) in visited:
        continue

    visited.add((node, sun))

    for dist, neighbor, is_above in graph[node]:
        new_sun = sun + (dist if is_above == 1 else 0)

        if new_sun > s:
            continue

        new_dist = d1 + dist
        if (neighbor, new_sun) not in distance or new_dist < distance[(neighbor, new_sun)]:
            distance[(neighbor, new_sun)] = new_dist
            heapq.heappush(pq, (new_dist, new_sun, neighbor))
else:
    print(-1)
    
#dijkstra??????