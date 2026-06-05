class Solution(object):
    def totalWaviness(self, num1, num2):
        
        def solve(x):
            if x < 100:
                return 0
            
            s = str(x)
            n = len(s)
            memo = {}
            
            def dp(idx, prev, prev2, is_less, is_started):
                if idx == n:
                    return 0, 1 if is_started else 0
                
                state = (idx, prev, prev2, is_less, is_started)
                if state in memo:
                    return memo[state]
                
                limit = 9 if is_less else int(s[idx])
                res_waviness = 0
                res_count = 0
                
                for d in range(limit + 1):
                    next_is_less = is_less or (d < limit)
                    
                    if not is_started:
                        if d == 0:
                            w, c = dp(idx + 1, -1, -1, next_is_less, False)
                            res_waviness += w
                            res_count += c
                        else:
                            w, c = dp(idx + 1, d, -1, next_is_less, True)
                            res_waviness += w
                            res_count += c
                    else:
                        w, c = dp(idx + 1, d, prev, next_is_less, True)
                        
                        if prev2 != -1:
                            if (prev > prev2 and prev > d) or (prev < prev2 and prev < d):
                                res_waviness += c
                                
                        res_waviness += w
                        res_count += c
                        
                memo[state] = (res_waviness, res_count)
                return memo[state]
            
            return dp(0, -1, -1, False, False)[0]
            
        return solve(num2) - solve(num1 - 1)
        