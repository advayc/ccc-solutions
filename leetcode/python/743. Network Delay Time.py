import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for node, connection, weight in times:
            graph[node].append((connection, weight))

        minheap = [(0, k)]
        mintimes = {}

        while minheap:
            timetonext, curnode = heapq.heappop(minheap)
            if curnode in mintimes:
                continue
            
            mintimes[curnode] = timetonext
            for neighbour, ntime in graph[curnode]:
                if neighbour not in mintimes:
                    heapq.heappush(minheap, (timetonext+ntime, neighbour))
            
        if len(mintimes) == n:
            return max(mintimes.values())
        else:
            return -1
