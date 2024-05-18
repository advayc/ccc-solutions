m = int(input()) # rows
n = int(input()) # cols
k = int(input())
grid = [['B' for _ in range(n)] for _ in range(m)]
ans=0
for i in range(k):
    direction,pos = map(str, input().split())
    pos=int(pos)-1 # indexing
    if direction == 'C':
        for ro in range(m):
            if grid[ro][pos] == 'B':
                grid[ro][pos]='G' # replace
            elif grid[ro][pos] == 'G':
                grid[ro][pos]='B' # replace
    elif direction == 'R':
        for col in range(n):
            if grid[pos][col] == 'B':
                grid[pos][col] = 'G' # replace
            elif grid[pos][col] == 'G':
                grid[pos][col] = 'B' # replace

for each in (grid):
    ans += each.count('G')
print(ans)
