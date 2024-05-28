n=int(input())
c=input()
cc=input()
ans=0
for i in range(n):
    if c[i] == 'C' and cc[i] == 'C':
        ans+=1
print(ans)
