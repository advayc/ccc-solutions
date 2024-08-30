class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
                return 0
            else:
                grid[r][c] = 0
                return 1 + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r - 1, c) + dfs(r, c + 1)

        n=0

        for ROWS in range(rows):
            for COLS in range(cols):
                if grid[ROWS][COLS] == 1:
                    n = max(n, dfs(ROWS, COLS))
        return n
