class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row_counts = [sum(row) for row in grid]
        col_counts = [sum(grid[i][j] for i in range(m)) for j in range(n)]
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (row_counts[i] > 1 or col_counts[j] > 1):
                    ans += 1
                    
        return ans