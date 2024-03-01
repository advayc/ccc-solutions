c = int(input())
r1 = list(map(int, input().split()))
r2 = list(map(int, input().split()))
sum = 0

for i in range(c):
    if r1[i] == 1 or r2[i] == 1:
        sum += 3

    if i % 2 == 0:
        if r1[i] and r2[i] == 1:
            sum -= 2

    if i > 0:
        if r1[i] and r1[i-1] or r2[i] and r2[i-1]:
            sum -= 1
    
    if i < c - 1:
        if r1[i] and r1[i+1] or r2[i] and r2[i+1]:
            sum -= 1
print(sum)