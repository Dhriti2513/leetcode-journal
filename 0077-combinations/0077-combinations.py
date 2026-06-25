class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        
        def backtrack(start, path):
            if len(path) == k:
                ans.append(list(path))
                return
                
            for i in range(start, n + 1):
                if len(path) + (n - i + 1) < k:
                    break
                path.append(i)
                backtrack(i + 1, path)
                path.pop()
                
        backtrack(1, [])
        return ans