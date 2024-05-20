n=(input())
k=int(input())
sum=0
for i in range(k+1):
    sum += int(n)
    n += '0'

print(sum)