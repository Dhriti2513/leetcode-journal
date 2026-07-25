class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Base cases for n <= 2
        if n <= 2:
            return n
            
        # For n >= 3, all values in [0, 2^bit_length - 1] can be formed
        return 1 << n.bit_length()