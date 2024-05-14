class Solution:
    def search(self, board: list[str], word: str):
        rows, colls = len(board), len(board[0])
        path = set() # make set bc cant revist anything in the path

        def dfs(r, c, i): # where i is the current char
            if i == len(word): #is on the last pos
                return True
            if (r<0 or c<0 or r>=rows or c>= colls or word[i] != board[r][c] or (r, c) in path): 
                # cant have a negative row/col. 
                # cant have row/col we on rn equal or larger to total row/coll. 
                # cant have letter in word[i] not in board cords 
                # cant have current cords be in path (means we already went there)
                return False
            
            path.add(r, c)# add current row/collum position bc we know it right 
            res = dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1)
            # found character so now we go to the next character. run this on each possible direction (1, 0)(-1,0)(0,1)(0,-1) (doesnt allow )
            path.remove(r,c)# leave position
            return res
        
        # now run this dfs for every single row and collum
        for ROW in range(rows):
            for COLLUM in range(colls):
                if dfs(ROW, COLLUM, 0):
                    return True
        return False
        
#2023 j5
word = input()
ROWS = int(input())
COLS = int(input())
grid = []
for _ in range(ROWS):
    grid.append(input().split())
t = 0


def dfs(cur_r, cur_c, dr, dc, i, turned):
    global t
    if cur_r < 0 or cur_c < 0 or cur_r >= ROWS or cur_c >= COLS or grid[cur_r][cur_c] != word[i]:
    # cant have a negative row/col. 
    # cant have row/col we on rn equal or larger to total row/coll. 
    # cant have letter in word[i] not in board cords 
        return 0
    if i+1 == len(word):
        t += 1
        return 0
    dfs(cur_r+dr, cur_c+dc, dr, dc, i+1, turned)
    if not turned:
        dfs(cur_r-dc, cur_c+dr, -dc, dr, i+1, True)
        dfs(cur_r+dc, cur_c-dr, dc, -dr, i+1, True)

for row in range(ROWS):
    for col in range(COLS):
        if grid[row][col] == word[0]:
            # run recersive function for every possible position
            dfs(row, col+1, 0, 1, 1, False) # up 1
            dfs(row+1, col, 1, 0, 1, False) # right 1
            dfs(row, col-1, 0, -1, 1, False) # left 1 
            dfs(row-1, col, -1, 0, 1, False) # down 1
            dfs(row+1, col+1, 1, 1, 1, False) # up 1 right 1
            dfs(row-1, col+1, -1, 1, 1, False) # up 1 left 1
            dfs(row-1, col-1, -1, -1, 1, False) # down 1 left 1
            dfs(row+1, col-1, 1, -1, 1, False) # down 1 right 1
print(t)