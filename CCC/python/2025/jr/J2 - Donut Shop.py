d=int(input())
e=int(input())

for i in range(e):
    x=(input())
    b=int(input())

    if x == '+':
        d+=b
    elif x =='-':
        d-=b

print(d)