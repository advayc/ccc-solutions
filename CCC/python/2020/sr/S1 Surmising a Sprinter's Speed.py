n = int(input())
a = []
for i in range(n):
    x, y = map(int, input().split())
    a.append((x, y))

a.sort()
ans = 0
for i in range(len(a) - 1):
    ans = max(ans, abs((a[i+1][1]-a[i][1])/(a[i+1][0]-a[i][0])))

print(ans)
