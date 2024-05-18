n=int(input())
for i in range(n):
    c=input()
    if len(c) > 10:
        print(c[0] + str(len(c)-2) + c[-1])
    else:
        print(c)