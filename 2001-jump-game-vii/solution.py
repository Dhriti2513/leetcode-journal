class Solution(object):
    def canReach(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """
        n = len(s)
        if s[n - 1] == '1':
            return False
            
        dp = [False] * n
        dp[0] = True
        reachable_count = 0
        
        for i in range(1, n):
            if i >= minJump and dp[i - minJump]:
                reachable_count += 1
            if i > maxJump and dp[i - maxJump - 1]:
                reachable_count -= 1
                
            if reachable_count > 0 and s[i] == '0':
                dp[i] = True
                
        return dp[n - 1]
