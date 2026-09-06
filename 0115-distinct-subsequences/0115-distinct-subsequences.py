class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(t)
        dp = [1] + [0] * m
        
        for char in s:
            for j in range(m, 0, -1):
                if char == t[j - 1]:
                    dp[j] += dp[j - 1]
                    
        return dp[m]