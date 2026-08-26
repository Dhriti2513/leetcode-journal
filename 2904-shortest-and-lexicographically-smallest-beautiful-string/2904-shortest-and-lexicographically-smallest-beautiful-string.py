class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones = [i for i, ch in enumerate(s) if ch == '1']
        
        # If there are fewer than k ones, return an empty string
        if len(ones) < k:
            return ""
        
        min_len = float('inf')
        best_str = ""
        
        # Step 2: Check every window of k consecutive 1s
        for i in range(len(ones) - k + 1):
            start = ones[i]
            end = ones[i + k - 1]
            sub = s[start : end + 1]
            
            # Step 3: Keep the shortest, lexicographically smallest substring
            if len(sub) < min_len:
                min_len = len(sub)
                best_str = sub
            elif len(sub) == min_len:
                best_str = min(best_str, sub)
                
        return best_str