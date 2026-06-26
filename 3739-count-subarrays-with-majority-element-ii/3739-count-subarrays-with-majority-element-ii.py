class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        freq = [0] * (2 * n + 1)
        freq[0 + n] = 1
        
        ans = 0
        current_sum = 0
        less_than_count = 0
        
        for num in nums:
            if num == target:
                less_than_count += freq[current_sum + n]
                current_sum += 1
            else:
                current_sum -= 1
                less_than_count -= freq[current_sum + n]
            
            ans += less_than_count
            freq[current_sum + n] += 1
            
        return ans