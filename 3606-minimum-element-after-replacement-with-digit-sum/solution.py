class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_sum = float('inf')
        
        for num in nums:
            current_sum = 0
            while num > 0:
                current_sum += num % 10
                num //= 10
            
            if current_sum < min_sum:
                min_sum = current_sum
                
        return min_sum
