import sys
input=sys.stdin.readline
n, m, k = map(int, input().split())
ans = []
for i in range(n):
    rem = n - i - 1
    cur = min(k - rem, m)
    if cur <= 0:
        break
    if cur > i:
        val = min(m, i + 1)
        cur = val
    else:
        val = ans[i - cur]
    ans.append(val)
    k -= cur

if k == 0 and len(ans) == n:
    print(*ans)
else:
    print(-1)