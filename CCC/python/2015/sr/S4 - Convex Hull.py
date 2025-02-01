import heapq
import sys
input=sys.stdin.readline

def dijk(s, e, md, g, n):
    dp = [[10**18] * md for _ in range(n + 1)]
    dp[s][0] = 0
    pq = [(0, s, 0)]
    while pq:
        t, cur, dmg = heapq.heappop(pq)
        if t != dp[cur][dmg]:
            continue
        if cur == e:
            return t
        for nxt, tt, dd in g[cur]:
            nd = dmg + dd
            if nd < md:
                nt = t + tt
                if nt < dp[nxt][nd]:
                    dp[nxt][nd] = nt
                    heapq.heappush(pq, (nt, nxt, nd))
    return -1

k, n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
for _ in range(m):
    a,b,t,h=map(int, input().split())
    g[a].append((b, t, h))
    g[b].append((a, t, h))
s, e = map(int, input().split())
print(dijk(s, e, k, g, n))