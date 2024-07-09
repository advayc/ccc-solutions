c,r = map(int, input().split())
borders = [(0,0),(0,r),(c,r),(c,0)] # b left, top left, top right, b right
# [(0, 0), (0, 200), (100, 200), (100, 0)]
px=0
py=0
x,y = map(int, input().split())

while x != 0 or y != 0:
    px += x 
    py += y
    if px < borders[0][0]:
        px = borders[0][0]
    if py < borders[0][1]:
        py = borders[0][1] # check if negative or less the 0,0

    if px < borders[1][0]:
        px = borders[1][0]
    if py > borders[1][1]:
        py = borders[1][1]

    if px > borders[2][0]:
        px = borders[2][0]
    if py > borders[2][1]:
        py = borders[2][1]

    if px > borders[3][0]:
        px = borders[3][0]
    if py < borders[3][1]:
        py = borders[3][1]

    print(px,py)
    x,y = map(int, input().split())

