class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        duplicate = -1
        missing = -1
        
        counts = [0] * (n + 1)
        for num in nums:
            counts[num] += 1
            
        for i in range(1, n + 1):
            if counts[i] == 2:
                duplicate = i
            elif counts[i] == 0:
                missing = i
                
        return [duplicate, missing]
