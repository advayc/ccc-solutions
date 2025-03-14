import heapq
from collections import defaultdict
import sys
input = sys.stdin.readline

def dijkstra(edges, start, end):
    graph = defaultdict(list)
    
    for a, b, c in edges:
        graph[a].append((b, c))
        graph[b].append((a, c))

    heap = []
    visited = set()
    
    #  considering all starting tunnels
    for neighbor, temp in graph[start]:
        heapq.heappush(heap, (abs(temp), neighbor, temp))

    while heap:
        cost, room, chill = heapq.heappop(heap)
        
        if (room, chill) in visited:
            continue
        visited.add((room, chill))
        
        if room == end:
            return cost
        
        # Move through tunnels with the same chilling level
        for neighbor, temp in graph[room]:
            if (neighbor, temp) not in visited:
                additional_cost = abs(chill - temp)
                heapq.heappush(heap, (cost + additional_cost, neighbor, temp))
    
    return -1

def bfs(edges, start, end):
    graph=defaultdict(list)

    for a, b, _ in edges:
        graph[a].append(b)
        graph[b].append(a)

    count=0
    q=[]
    visited=set()
    q.append((start, count))
    visited.add(start)
    while q:
        cur=q.pop(0)
        if cur == end:
            return count
        for neighbour in graph[cur]:
            if neighbour not in visited:
                q.append((cur, count+1))
                visited.add(cur)
    return -1
    
n, m = map(int, input().split())

edges = []
for _ in range(m):
    edges.append(tuple(map(int, input().split())))

if m == n-1:
    print(bfs(edges, 1, n))
else:
    print(dijkstra(edges, 1, n))