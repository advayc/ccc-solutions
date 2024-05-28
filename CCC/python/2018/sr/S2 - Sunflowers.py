def rotate_grid(grid):
    N = len(grid)
    # Check the edges to determine the rotation
    first_row = grid[0]
    last_row = grid[N - 1]
    first_col = [grid[i][0] for i in range(N)]
    last_col = [grid[i][N - 1] for i in range(N)]
    
    if first_col == sorted(first_col):
        # 90 degrees clockwise
        return [[grid[N - j - 1][i] for j in range(N)] for i in range(N)]
    elif first_row == sorted(first_row):
        # 0 degrees
        return grid
    elif last_col == sorted(last_col, reverse=True):
        # 90 degrees counterclockwise
        return [[grid[j][N - i - 1] for j in range(N)] for i in range(N)]
    elif last_row == sorted(last_row, reverse=True):
        # 180 degrees
        return [[grid[N - i - 1][N - j - 1] for j in range(N)] for i in range(N)]

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

original_grid = rotate_grid(grid)
for row in original_grid:
    print(' '.join(map(str, row)))
