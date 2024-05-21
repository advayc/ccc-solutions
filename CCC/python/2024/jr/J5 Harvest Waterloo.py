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