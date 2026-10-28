class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # dp[j] will store the set of all possible XOR path values at row i, column j
        dp = [set() for _ in range(n)]
        
        # Base case for the top-left cell
        dp[0].add(grid[0][0])
        
        # Initialize the first row
        for j in range(1, n):
            dp[j] = {val ^ grid[0][j] for val in dp[j - 1]}
            
        # Fill the rest of the grid
        for i in range(1, m):
            # First column of current row depends only on the cell above
            dp[0] = {val ^ grid[i][0] for val in dp[0]}
            
            for j in range(1, n):
                # Union of paths coming from the top (dp[j]) and left (dp[j-1])
                prev_vals = dp[j].union(dp[j - 1])
                dp[j] = {val ^ grid[i][j] for val in prev_vals}
                
        return min(dp[n - 1])