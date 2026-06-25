class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        n = len(s)
        
        if n < 4 or n > 12:
            return ans
            
        def backtrack(start, path):
            if len(path) == 4:
                if start == n:
                    ans.append(".".join(path))
                return
                
            for length in range(1, 4):
                if start + length > n:
                    break
                    
                segment = s[start:start+length]
                
                if (segment[0] == '0' and len(segment) > 1) or int(segment) > 255:
                    continue
                    
                path.append(segment)
                backtrack(start + length, path)
                path.pop()
                
        backtrack(0, [])
        return ans