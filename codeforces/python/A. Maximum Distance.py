import math,sys
n = int(sys.stdin.readline())
x_coords = list(map(int, sys.stdin.readline().split()))
y_coords = list(map(int, sys.stdin.readline().split()))
maxs=[]
for i in range(n):
    for j in range(i+1,n):
        x = (x_coords[i] - x_coords[j]) **2
        y = (y_coords[i] - y_coords[j]) **2
        maxs.append(math.sqrt(x+y))# check if the prev max is bigger then the current sq
    
print(round(max(maxs)**2))
# O(N^2) so using sys.stdin.readline() but still TLE
# submit on pypy so doesnt TLE