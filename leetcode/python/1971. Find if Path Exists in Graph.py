from collections import deque, defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        graph = [[] for _ in range(n+1)]
        for node, connection in edges:
            graph[node].append(connection)
            graph[connection].append(node)

        q=deque()
        q.append(source)
        visited=set()
        visited.add(source)
        while q:
            cur=q.popleft()
            if destination == cur:
                return True
            for neighbour in graph[cur]:
                if neighbour not in visited:
                    q.append(neighbour)
                    visited.add(neighbour)
        return False