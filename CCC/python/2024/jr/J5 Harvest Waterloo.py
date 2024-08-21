# recursive solution with a DFS
import sys 
input=sys.stdin.readline
sys.setrecursionlimit(10000)
rows = int(input())
cols = int(input())
grid = [list(input()) for i in range(rows)]
y=int(input())
x=int(input())
values={'S':1, 'M': 5, 'L': 10}
total=0

def go(ROW,COL):
    global total
    total += values[grid[ROW][COL]]
    grid[ROW][COL]='*'

    if COL + 1 < cols and grid[ROW][COL+1] != '*':
        go(ROW,COL+1)
    if COL - 1 >=0 and grid[ROW][COL-1] != '*':
        go(ROW,COL-1)
    if ROW+1 < rows and grid[ROW+1][COL] != '*':
        go(ROW+1,COL)
    if ROW-1 >= 0 and grid[ROW-1][COL] != '*':
        go(ROW-1,COL)

go(y,x)
print(total)

# iteratve solution with a BFS
r=int(input())
c=int(input())
patch=[input() for _ in range(r)]
pumpkin_values = {'S': 1, 'M': 5, 'L': 10}
total=0
directions=[(0,1),(1,0),(0,-1),(-1,0)]
a=int(input())
b=int(input())
q=[(a,b)]
visited=set([(a,b)])
while q:
    x,y=q.pop(0)
    if patch[x][y] in pumpkin_values:
        total += pumpkin_values[patch[x][y]]
    
    for dx,dy in directions:
        nx,ny = dx+x,dy+y
        if 0 <= nx < r and 0 <= ny < c and patch[nx][ny] != '*' and (nx,ny) not in visited:
            q.append((nx,ny))
            visited.add((nx,ny))
print(total)
