word = 'VASES'
board = [   ['H', 'I', 'W', 'H'],
       	    ['P', 'X', 'B', 'Y'],
        	['A', 'S', 'Q', 'K'],
        	['P', 'V', 'E', 'S'] ]

moves=[(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]
rows = len(board)
cols = len(board[0])
visited = [[False for _ in range(rows)] for x in range(cols)] # we can use a visited 2d array or use a set to show our path

def dfs(row, col, cur_pos): # cur_pos is just the index of the string where we are currently on. 
    if cur_pos == len(word):
        return
    
    if board[row][col] == word[cur_pos]:
        for x,y in moves:
            if 0 <= row+x < rows or 0 <= col+y < cols and not visited: 
                # if weve been there, if the next pos is not in the grid, if next pos negative
                visited[row][col] = True
                dfs(row+x,col+y,cur_pos+1)
                visited[row][col] = False

for ROW in range(rows):
    for COL in range(cols):
        if dfs(ROW,COL,0):
            found = True
        else:
            found = False

if found:
    print('There is an occurance of the word',word)
else:
    print('There is NOT an occurance of the word',word)
