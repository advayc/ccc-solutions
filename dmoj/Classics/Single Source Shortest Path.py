import heapq

def dijkstra(n, graph):
    dist = [float('inf')] * n
    dist[0] = 0
    queue = [(0, 0)]  # (distance, node)

    while queue:
        d, node = heapq.heappop(queue)
        if d != dist[node]:
            continue
        for nei, w in graph[node]:
            if dist[node] + w < dist[nei]:
                dist[nei] = dist[node] + w
                heapq.heappush(queue, (dist[nei], nei))

    return dist

def solve():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append((v, w))
        graph[v].append((u, w))

    dist = dijkstra(n, graph)
    for d in dist:
        print(-1 if d == float('inf') else d)

solve()