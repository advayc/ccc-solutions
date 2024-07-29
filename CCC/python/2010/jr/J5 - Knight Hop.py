start_x, start_y=map(int, input().split())
end_x, end_y=map(int, input().split())
directions = [(1,2),(1,-2),(2,1),(2,-1),(-1,2),(-1,-2),(-2,1),(-2,-1)]
queue=[]
queue = [(start_x, start_y, 0)]  # (current_row, current_col, number_of_moves)
visited = set()
visited.add((start_x, start_y))
while queue:
    x,y,moves = queue.pop(0)
    if (x,y) == (end_x,end_y):
        print(moves)
        break
    for dx,dy in directions: # go through every move to see if it works, keep doing this till the startx,starty equal the endx and endy
        newx = x+dx
        newy = y+dy
        if 1 <= newx <= 8 and 1 <= newy <= 8 and (newx, newy) not in visited:
            queue.append((newx,newy, moves+1))
            visited.add((newx,newy))