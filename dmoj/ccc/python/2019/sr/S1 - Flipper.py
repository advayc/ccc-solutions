grid = [[1, 2], [3, 4]]

for action in input():
    if action == "H":
        grid.append(grid.pop(0))
    elif action == "V":
        grid[1].append(grid[1].pop(0))
        grid[0].append(grid[0].pop(0))
for i in grid:
    print(i[0], i[1])
