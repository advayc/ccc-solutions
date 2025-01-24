import sys
# dont even work
input = sys.stdin.readline
M = int(input())

edges = []

for i in range(M):
    line = list(map(int, input().split()))
    e = line[0]
    corners = line[1:e + 1]
    weights = line[e + 1:]

    corners.append(corners[0])

    for j in range(e):
        u = corners[j]
        v = corners[j + 1]
        weight = weights[j]
        if u > v:
            u, v = v, u
        edges.append((weight, u, v))
        edges.append((weight, 0, corners[j]))  #connect each corner to the outside (node 0)

parent = list(range(1001))
size = [1] * 1001

edges.sort()
min_cost = 0

for weight, u, v in edges:
    root_u = u
    while parent[root_u] != root_u:
        root_u = parent[root_u]

    root_v = v
    while parent[root_v] != root_v:
        root_v = parent[root_v]

    if root_u != root_v:
        if size[root_u] > size[root_v]:
            parent[root_v] = root_u
            size[root_u] += size[root_v]
        else:
            parent[root_u] = root_v
            size[root_v] += size[root_u]
        min_cost += weight

print(weight+1)