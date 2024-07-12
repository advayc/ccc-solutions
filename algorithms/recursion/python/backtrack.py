word = 'ABCCED'
board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
rows = len(board)
col = len(board[0])
def dfs(row, col, cur_pos):
    if cur_pos == len(word):
        return
    
