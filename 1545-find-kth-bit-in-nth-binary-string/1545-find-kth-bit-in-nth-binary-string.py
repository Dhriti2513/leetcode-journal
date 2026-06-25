class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n == 1:
            return "0"
            
        length = (1 << n) - 1
        mid = length // 2 + 1
        
        if k == mid:
            return "1"
        elif k < mid:
            return self.findKthBit(n - 1, k)
        else:
            corresponding_k = length - k + 1
            bit = self.findKthBit(n - 1, corresponding_k)
            return "1" if bit == "0" else "0"