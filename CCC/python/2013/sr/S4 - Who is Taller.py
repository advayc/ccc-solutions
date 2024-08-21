# https://dmoj.ca/problem/ccc13s4

from collections import deque
import sys
input = sys.stdin.readline

nodes, edges = map(int, input().split())
graph = [[] for _ in range(nodes+1)]

for i in range(edges):
    l, s = map(int, input().split())
    graph[l].append(s)

start, end = map(int, input().split())

def bfs(start, end, graph):
    visited = set()
    q=deque([start])
    visited.add(start)
    while q:
        cur = q.popleft()
        if cur == end:
            return True
        for neighbour in graph[cur]:
            if neighbour not in visited:
                visited.add(neighbour)
                q.append(neighbour)
    return False

reachable_from_start = bfs(start,end,graph)
reachable_from_end = bfs(end,start,graph)

if reachable_from_start:
    print('yes')
elif reachable_from_end:
    print('no')
else:
    print('unknown')