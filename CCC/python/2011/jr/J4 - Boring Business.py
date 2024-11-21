# basically just first apply all the transitions to the points ie show the points where u supposed to go, then loop through the number of units and include the path to those x and y in the list of disallowed quords

passed = [[0,-1], [0,-2], [0,-3], [1,-3], [2,-3], [3,-3], [5,-3], [6,-3], [7,-3], 
          [3,-4], [5,-4], [7,-4], [-1,-5], [3,-5], [4,-5], [5,-5], [7,-5], 
          [-1,-6], [7,-6], [-1,-7], [0,-7], [1,-7], [2,-7], [3,-7], [4,-7], 
          [5,-7], [6,-7], [7,-7]]

current_X, current_Y = -1, -5
dx, dy = -1, -5
status = 'safe'

while status != 'DANGER':
    direction, units = input().split()
    units = int(units)
    status = 'safe'

    if direction == 'l':
        dx = (dx - units)
    elif direction == 'd':
        dy = (dy - units)
    elif direction == 'u':
        dy = (dy + units)
    elif direction == 'r':
        dx = (dx + units)
    elif direction == 'q':
        status = "DANGER"
        break

    for _ in range(units):
        if direction == 'l':
            current_X -= 1
        elif direction == 'r':
            current_X += 1
        elif direction == 'u':
            current_Y += 1
        elif direction == 'd':
            current_Y -= 1
    
        if [current_X, current_Y] in passed:
            status = "DANGER"
            break
        else:
            passed.append([current_X, current_Y])

    print(dx, dy, status)