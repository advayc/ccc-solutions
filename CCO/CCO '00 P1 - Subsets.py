from collections import defaultdict

n = int(input())
di = defaultdict(list)

#build graph
for _ in range(n):
    x, y = input().split(" contains ")
    di[x].append(y)
    if y.isupper() and y not in di:
        di[y] = []

for key in sorted(di.keys()):
    elements = set()
    q = [key]
    visited = set()
    visited.add(key)
    
    while q:
        curr = q.pop(0)
        for ele in di[curr]:
            if ele.islower():# If it's an element, add to the set
                elements.add(ele)
            elif ele not in visited:
                q.append(ele)
                visited.add(ele)
    
    print(f"{key} = " + "{" + ",".join(sorted(elements)) + "}")