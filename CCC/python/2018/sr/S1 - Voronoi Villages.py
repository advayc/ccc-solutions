n=int(input())
ne = [int(input()) for _ in range(n)]
ne.sort()
x=[]
for i in range(1, n - 1):
    left = (ne[i] - ne[i - 1]) / 2
    right = (ne[i + 1] - ne[i]) / 2
    size = left + right
    x.append(size)

min_size = min(x)
print(min_size)