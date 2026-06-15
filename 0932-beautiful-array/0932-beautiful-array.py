class Solution(object):
    def beautifulArray(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [1]
        
        while len(result) < n:
            odds = [2 * x - 1 for x in result]
            evens = [2 * x for x in result]
            result = odds + evens
            
        return [x for x in result if x <= n]