class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perm = 0
        rows, collums = len(grid), len(grid[0])

        for row in range(rows):
            for col in range(collums):
                if grid[row][col] == 1:
                    perm += 4
                    if row >0 and grid[row-1][col] == 1:
                        perm -=2
                    if col>0 and grid[row][col-1]==1:
                        perm -= 2
        return perm