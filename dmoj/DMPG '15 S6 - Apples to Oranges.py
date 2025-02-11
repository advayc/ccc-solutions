import math
from collections import deque
N, M = map(int, input().split())
fruits = [input().strip() for _ in range(N)]
fruit_index = {fruits[i]: i for i in range(N)}
edges = []
graph = [[] for _ in range(N)]
rev = [[] for _ in range(N)]
for _ in range(M):
    u_name, v_name, rate_str = input().split()
    rate = float(rate_str)
    u = fruit_index[u_name]
    v = fruit_index[v_name]
    w = -math.log(rate)
    edges.append((u, v, w))
    graph[u].append(v)
    rev[v].append(u)
INF = float('inf')
dist = [INF] * N
source = fruit_index["APPLES"]
dist[source] = 0.0
for _ in range(N - 1):
    changed = False
    for u, v, w in edges:
        if dist[u] + w < dist[v] - 1e-12:
            dist[v] = dist[u] + w
            changed = True
    if not changed:
        break
arb = [False] * N
for u, v, w in edges:
    if dist[u] + w < dist[v] - 1e-12:
        arb[v] = True
q = deque()
for i in range(N):
    if arb[i]:
        q.append(i)
while q:
    u = q.popleft()
    for v in graph[u]:
        if not arb[v]:
            arb[v] = True
            q.append(v)
can_reach = [False] * N
q = deque([source])
can_reach[source] = True
while q:
    u = q.popleft()
    for v in rev[u]:
        if not can_reach[v]:
            can_reach[v] = True
            q.append(v)
res = False
for i in range(N):
    if arb[i] and can_reach[i]:
        res = True
        break
print("YA" if res else "NAW")