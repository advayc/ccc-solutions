def bfs(grid, rows,cols):
    distances = {
        '+': [(0,1), (1,0), (-1,0), (0,-1)],
        '|': [(1,0), (-1,0)],
        '-': [(0,1), (0,-1)],
        '*': [],
    }
    visited = set()
    visited.add((0,0))
    q = [(0,0,0)] # row col distance

    while q:
        x,y,d = q.pop(0)

        if x == rows-1 and y == cols-1:
            return d+1# if weve hit the bottom left corner 

        for dx, dy in distances[grid[x][y]]:
            newx = x + dx
            newy = y + dy

            if 0 <= newx < rows and 0 <= newy < cols and (newx,newy) not in visited and grid[newx][newy] != '*':
                visited.add((newx, newy))
                q.append((newx, newy, d + 1))
    return -1
    
n = int(input())
res=[]

for i in range(n):
    rows=int(input())
    cols=int(input())
    grd = [input().strip() for _ in range(rows)]
    res.append(bfs(grd, rows, cols))

for i in res:
    print(i)