# https://dmoj.ca/problem/vmss7wc16c3p2

houses, roads, start, end = map(int, input().split())
graph = {}
    
for i in range(houses+1):
    graph[i] = []

for _ in range(roads):
    node, connection = map(int, input().split())
    graph[node].append(connection)
    graph[connection].append(node)

def bfs(start, end):
    q = []
    visited = set()
    visited.add(start)
    q.append(start)
    while q:
        current = q.pop(0)
        if current == end:
            return 'GO SHAHIR!'
        for neighbour in graph[current]:
            if neighbour not in visited:
                visited.add(neighbour)
                q.append(neighbour)
    return 'NO SHAHIR!'

print(bfs(start, end))
