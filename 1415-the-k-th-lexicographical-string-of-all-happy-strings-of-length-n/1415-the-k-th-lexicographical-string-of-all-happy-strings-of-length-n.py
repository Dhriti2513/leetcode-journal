class Solution(object):
    def getHappyString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ans = []
        
        def backtrack(path):
            if len(path) == n:
                ans.append("".join(path))
                return
            if len(ans) == k:
                return
                
            for char in ['a', 'b', 'c']:
                if not path or path[-1] != char:
                    path.append(char)
                    backtrack(path)
                    path.pop()
                    
        backtrack([])
        return ans[k - 1] if len(ans) >= k else ""