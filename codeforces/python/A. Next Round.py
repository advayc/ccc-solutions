n,k=map(int, input().split())
c=list(map(int, input().split()))
ans=0
for i in c:
    if i >= c[k-1] and i > 0:
        ans += 1
print(ans)
