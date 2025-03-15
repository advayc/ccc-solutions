n = int(input()) 
weather = [input().strip() for _ in range(n)]
a, b, c = [0]*n, [0]*n, 0
if weather[0] == 'S':
    a[0] = 1
for i in range(1, n):
    if weather[i] == 'S':
        a[i] = a[i - 1] + 1
if weather[n - 1] == 'S':
    b[n - 1] = 1
for i in range(n - 2, -1, -1):
    if weather[i] == 'S':
        b[i] = b[i + 1] + 1
for i in range(1, n-1): 
    if weather[i] == 'P':
        x = a[i - 1] + 1 + b[i + 1]
        c = max(c, x)
print(c)