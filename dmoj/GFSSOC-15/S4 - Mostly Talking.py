# https://dmoj.ca/problem/gfssoc2s4
import heapq
n, m = map(int, input().split())
graph = {}
for i in range(m):
    node, connection, weight = map(int, input().split())
    graph.update({(node): (weight, (connection))})

d = int(input())
for i in range(d):
    node, connection, weight = map(int, input().split())
    graph.update({(node): (weight, (connection))})

distances = {}
for i in range(1, n+1):
    distances[i] = float('inf')

distances[1] = 0
priority_q = [(0,1)]

while priority_q:
    current_dist, current_node = heapq.heappop(priority_q) # pop from the priority q

    if current_dist > distances[current_node]:
        continue

    for node, weight in graph[current_node].items():
        newdistance = weight + current_dist
        if newdistance < distances[node]:
            distances[node] = newdistance
            heapq.heappush(priority_q, (newdistance, node))

shortest = distances[n]

if shortest == float('inf'):
    print(-1)
else:
    print(shortest)

print(distances)
print(graph)

