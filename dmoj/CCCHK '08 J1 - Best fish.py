n=int(input())
totaln=[]
totalb=[]
for i in range(n):
    x,y=map(int, input().split())
    totaln.append(x*y)
c=int(input())
for i in range(c):
    a,b=map(int, input().split())
    totalb.append(a*b)
casp=max(totaln)
natal=max(totalb)
if casp > natal:
    print('Casper')
elif casp < natal:
    print('Natalie')
else:
    print('Tie')