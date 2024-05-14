n = int(input())
count = 0
for i in range(n):
    a, b, c = map(int, input().split())
    bruh = a+b+c
    if bruh >= 2:
        count += 1
        
print(count)