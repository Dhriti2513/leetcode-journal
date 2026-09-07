class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        # dp[i] stores count of distinct subsequences ending with character chr(ord('a') + i)
        dp = [0] * 26
        
        for char in s:
            idx = ord(char) - ord('a')
            # New count for subsequences ending in 'char'
            dp[idx] = (sum(dp) + 1) % MOD
            
        return sum(dp) % MOD