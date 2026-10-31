class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        INVALID = (-1, -1)

        destR = [[INVALID] * n for _ in range(m)]
        destD = [[INVALID] * n for _ in range(m)]

        # Precompute final landing positions
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 0:
                    destR[i][j] = (i, j)
                    destD[i][j] = (i, j)
                else:
                    if i + 1 < m:
                        destR[i][j] = destD[i + 1][j]

                    if j + 1 < n:
                        destD[i][j] = destR[i][j + 1]

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if dp[i][j] == 0:
                    continue

                cur = dp[i][j]

                # Move right
                if j + 1 < n:
                    r, c = destR[i][j + 1]
                    if r != -1:
                        dp[r][c] = (dp[r][c] + cur) % MOD

                # Move down
                if i + 1 < m:
                    r, c = destD[i + 1][j]
                    if r != -1:
                        dp[r][c] = (dp[r][c] + cur) % MOD

        return dp[m - 1][n - 1]