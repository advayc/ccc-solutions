import sys
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n+1)]
while True:
    start, end = map(int, input().split())
    if start == 0 and end == 0:
        break
    graph[start].append(end)

stack = [1]
total = [0] * (n+1)
total[1] = 1

while stack:
    cur=stack.pop()
    for nei in graph[cur]:
        total[nei] += total[cur]
        stack.append(nei)

print(total[n])