flooring_meters = int(input())
r = int(input())
c = int(input())
grid=[]
visited = [[False for w in range(c)] for e in range(r)]
walls=0
space=0

for i in range(r):
    line = input()
    line=list(line)
    grid.extend([line])
    for d in range (len(grid)):
        walls += grid[i][d].count('.')
        space += grid[i][d].count('I')

def check(x,y):
    global grid, visited
    if grid[x][y] == '.' and visited[x][y] == False:
        visited[x][y] = True # if weve been here in room space mark true in visited
        total=1
        for (direction_x, direction_y) in ((-1,0),(1,0),(0,1),(0,-1)):
            if (direction_x+x) >= 0 and (direction_x+x) < c and (direction_y+y) >=0 and (direction_y+y) < r:
                total += check(x+direction_x,y+direction_y)
        return total
    else:
        return 0
    
rooms =[]
for row in range(r):
    for col in range(c):
        room = check(row,col)
        if room >0:
            rooms.append(room)

rooms.sort(reverse=True)
remaining=flooring_meters
largest = 0
for room in rooms:
    if remaining >= room:
        largest +=1
        remaining -= room  
    else:
        break

if largest == 1:
    print('1 room', remaining, 'square meter(s) left over')
else:
    print(largest, 'rooms,', remaining, 'square meter(s) left over')
