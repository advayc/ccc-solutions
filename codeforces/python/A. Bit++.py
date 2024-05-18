n=int(input())
sum=0
for i in range(n):
    op = list(input())
    for j in op:
        if j == '+':
            sum +=1
            break
        elif j == '-':
            sum -= 1
            break
print(sum)