# https://dmoj.ca/problem/gfssoc2s4

# i dont know why this doesnt work -> works on first case

import sys
import heapq
input = sys.stdin.readline
n, m = map(int, input().split())
graph = {}

def dijkstra(start, graph, n):
    distances={}
    for i in range(1, n+1):
        distances[i] = float('inf') # make each node start off with infinity weight
    distances[start] = 0
    priority_q = [(0, start)]  # (distance, node)

    while priority_q:
        current_dist, current_node = heapq.heappop(priority_q)

        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            new_distance = current_dist + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(priority_q, (new_distance, neighbor))

    return distances

for i in range(1, n + 1):
    graph[i] = {}

for i in range(m):
    node, connection, weight = map(int, input().split())
    if connection not in graph[node] or graph[node][connection] > weight:
        graph[node][connection] = weight

d = int(input())
for i in range(d):
    node, connection, weight = map(int, input().split())
    if connection not in graph[node] or graph[node][connection] > weight:
        graph[node][connection] = weight

dist_from_start = dijkstra(1, graph, n)
rev={}
for i in range(1, n+1): # reverse graph
    rev[i] = {}

for u in graph:
    for v in graph[u]:
        if u not in rev[v] or rev[v][u] > graph[u][v]:
            rev[v][u] = graph[u][v]

dist_from_end = dijkstra(n, rev, n)

best_distance = float('inf')
for u in graph:
    for v in graph[u]:
        weight = graph[u][v]
        if dist_from_start[u] != float('inf') and dist_from_end[v] != float('inf'):
            best_distance = min(best_distance, dist_from_start[u] + weight + dist_from_end[v])

if best_distance == float('inf'):
    print(-1) #if no path found
else:
    print(best_distance)

