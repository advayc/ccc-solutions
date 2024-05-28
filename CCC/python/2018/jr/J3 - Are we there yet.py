nums = list(map(int, input().split()))
sumx=[0, sum(nums[:1]), sum(nums[:2]), sum(nums[:3]), sum(nums[:4])]
z=[]
for i in sumx:
    y=[]
    for j in sumx:
        y.append(str(abs(i-j)))
    z.append(' '.join(y))
for r in z:
    print(r)