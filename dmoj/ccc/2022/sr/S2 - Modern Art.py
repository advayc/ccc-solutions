import sys
# faster plz
m = int(sys.stdin.readline())  # rows
n = int(sys.stdin.readline())  # cols
k = int(sys.stdin.readline())
ans=0
grid = [['B' for _ in range(n)] for _ in range(m)]
row_changes = [0] * m
col_changes = [0] * n

for i in range(k):
    direction, pos = sys.stdin.readline().split()
    pos = int(pos) - 1  # indexing
    if direction == 'C':
        col_changes[pos] += 1
    elif direction == 'R':
        row_changes[pos] += 1

for row in range(m):
    for col in range(n):
        if (row_changes[row] + col_changes[col]) % 2 == 1:
            if grid[row][col] == 'B':
                grid[row][col] = 'G'
                ans += 1
            else:
                grid[row][col] = 'B'

print(ans)
