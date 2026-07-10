class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        max_len = 0
        
        for num in num_set:
            # Check if 'num' is the start of a sequence
            if num - 1 not in num_set:
                curr_num = num
                curr_len = 1
                
                # Incrementally look for the rest of the sequence
                while curr_num + 1 in num_set:
                    curr_num += 1
                    curr_len += 1
                    
                max_len = max(max_len, curr_len)
                
        return max_len