import itertools, sys
input = sys.stdin.readline
n=int(input())
k=int(input())
con=[tuple(map(int, input().split())) for _ in range(k)]
permutations = itertools.permutations(range(1,n+1)) # generate every permutation
c=0
for perm in permutations: # go through each permutations and check wether the index of x is higher then the index of y, meaning that x is after y, so its untrue
    val=True
    for x,y in con:
        if perm.index(x) > perm.index(y):
            val = False
            break

    if val:
        c+=1
print(c)

