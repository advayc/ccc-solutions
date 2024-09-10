n, m, k = map(int, input().split())
grid = [list(input()) for _ in range(n)]
new_grid = [['.' for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        cur = grid[i][j]
        if cur == '.':
            new_grid[i][j] = '.'

        if cur == 'A':
            if j + k < m: 
                scaled = grid[i][j+k]

                if scaled == 'B':
                    new_grid[i][j] = 'N'  
                else:
                    new_grid[i][j] = 'Y'  
            else:
                new_grid[i][j] = 'Y'

        if cur == 'B':
            if j - k >= 0:  
                scaled = grid[i][j-k]

                if scaled == 'A':
                    new_grid[i][j] = 'N'  
                else:
                    new_grid[i][j] = 'Y' 
            else:
                new_grid[i][j] = 'Y'  

for row in new_grid:
    print(''.join(row))