t = input()
n=len(t)
c=[]
for i in range(n):
    for j in range(n):
        x=t[i:j+1]
        if x == ''.join(reversed(x)):
            c.append(len(x))
print(max(c))