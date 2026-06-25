class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        transformed = [1 if x == target else -1 for x in nums]
        ans = 0
        n = len(transformed)
        
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += transformed[j]
                if current_sum > 0:
                    ans += 1
                    
        return ans