from collections import deque
import sys
input=sys.stdin.readline
def simulate_conveyor(x, y):
    visited_cells = set()
    while grid[x][y] in "LRUD":
        if (x, y) in visited_cells:
            return None
        visited_cells.add((x, y))
        d = grid[x][y]
        if d == "L":
            nx, ny = x, y - 1
        elif d == "R":
            nx, ny = x, y + 1
        elif d == "U":
            nx, ny = x - 1, y
        else:  # d == "D"
            nx, ny = x + 1, y
        if grid[nx][ny] not in ".SLRUD":
            return None
        x, y = nx, ny
    return (x, y)

rows, cols = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(rows)]
camera_seen = [[False]*cols for _ in range(rows)]
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == "C":
            for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
                a, b = i, j
                while True:
                    a += dx; b += dy
                    if a < 0 or a >= rows or b < 0 or b >= cols or grid[a][b] == "W":
                        break
                    if grid[a][b] in ".S":
                        camera_seen[a][b] = True
# find starting position
startX = startY = None
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == "S":
            startX, startY = i, j
            break
    if startX is not None:
        break

#fix robot start seen problem cuz it be gets caught from the start, so no moves possible
if camera_seen[startX][startY]:
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == ".":
                print(-1)
    sys.exit(0)

# do a bfs with steps counted
dist = [[-1]*cols for _ in range(rows)]
q = deque()
dist[startX][startY] = 0
q.append((startX, startY))
while q:
    cx, cy = q.popleft()
    for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
        nx, ny = cx + dx, cy + dy
        if not (0 <= nx < rows and 0 <= ny < cols):
            continue
        if grid[nx][ny] not in ".LRUDS":
            continue
        if grid[nx][ny] in ".S" and camera_seen[nx][ny]:
            continue
        finalPos = (nx, ny)
        if grid[nx][ny] in "LRUD":
            result = simulate_conveyor(nx, ny)
            if result is None:
                continue
            finalPos = result
            fx, fy = finalPos
            if grid[fx][fy] in ".S" and camera_seen[fx][fy]:
                continue
        fx, fy = finalPos
        if dist[fx][fy] == -1:
            dist[fx][fy] = dist[cx][cy] + 1
            q.append((fx, fy))
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == ".":
            print(dist[i][j])
