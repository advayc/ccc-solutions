# dfs with alternating between g or b
import sys
sys.setrecursionlimit(300000)
input=sys.stdin.readline
nodes, connection = map(int, input().split())
graph = [[] for _ in range(nodes+1)]
ans = ['G'] * connection # default the answer to be G

for index in range(connection):
    u,v = map(int, input().split())
    graph[u].append((v, index))
    graph[v].append((u, index))

visited = set()

def dfs(current, iss):
    for neighbour, index in graph[current]:
        if neighbour in visited:
            continue
        visited.add(neighbour)
        
        if ans[index] == 'G':
            if iss:
                ans[index] = 'R'
            else:
                ans[index] = 'B' # alternate coloring R then B 

        dfs(neighbour, not iss)
        
for node in range(1, nodes+1):
    if node not in visited:
        visited.add(node)
        dfs(node, True)
print(''.join(ans))