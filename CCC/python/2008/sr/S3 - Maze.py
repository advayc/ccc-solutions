def bfs(grid, r,c):
    distances = {
        '+': [(0,1), (1,0), (-1,0), (0,-1)],
        '-': [(1,0), (-1,0)],
        '|': [(0,1), (0,-1)],
        '*': [],
    }

    visited = set((0,0))
    q = [(0,0,0)] # row col distance

    while q:
        x,y,d = q.pop(0)

        if x == r-1 and y == c-1:
            return d# if weve hit the bottom left corner 

        for dx, dy in distances[grid[x][y]]:
            newx = x + dx
            newy = y + dy

            if 0 <= newx < r and 0 <= newy < c and (newx,newy) not in visited and grid[x][y] != '*':
                visited.add((newx, newy))
                q.append((newx, newy, d + 1))
    return -1
    
n = int(input())

for i in range(n):
    rows=int(input())
    cols=int(input())
    grd = [input().strip() for _ in range(rows)]
    print(bfs(grd, rows, cols))