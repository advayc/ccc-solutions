import sys
input = sys.stdin.readline

n, q = map(int, input().split())
cheese = [[[True]*n for _ in range(n)] for _ in range(n)]

def check_brick(x, y, z, dx, dy, dz):
    if x + dx > n or y + dy > n or z + dz > n:
        return False
    for i in range(dx):
        for j in range(dy):
            for k in range(dz):
                if cheese[x+i][y+j][z+k]:
                    return False
    return True

for _ in range(q):
    x, y, z = map(int, input().split())
    cheese[x][y][z] = False
    count = 0
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if check_brick(x, y, z, 1, 1, n-z):
                    count += 1
                    
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if check_brick(x, y, z, n-x, 1, 1):
                    count += 1
                    
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if check_brick(x, y, z, 1, n-y, 1):
                    count += 1
    print(count)