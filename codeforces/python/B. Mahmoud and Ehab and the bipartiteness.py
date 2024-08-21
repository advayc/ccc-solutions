n=int(input())
graph=[[] for _ in range(n+1)]
for x in range(n-1):
    node, connection = map(int, input().split())
    graph[node].append(connection)
    graph[connection].append(node)

colored=[-1]*(n+1)

q=[1]
visited=set()
visited.add(1)
colored[1]=0
cnta=1
cntb=0

while q:
    cur = q.pop(0)
    current = colored[cur]
    for neighbour in graph[cur]:
        if neighbour not in visited:
            visited.add(neighbour)
            colored[neighbour] = 1-current
            if colored[neighbour] == 0:
                cnta += 1
            else:
                cntb += 1
            q.append(neighbour)
max_edges = cnta * cntb - (n - 1)
print(max_edges)
