class Solution(object):
    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Helper function to compute GCD so it works perfectly in Python 2
        def get_gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        prefix_gcd = []
        mx = 0
        
        # Step 1: Construct prefixGcd array
        for num in nums:
            if num > mx:
                mx = num
            prefix_gcd.append(get_gcd(num, mx))
            
        # Step 2: Sort in non-decreasing order
        prefix_gcd.sort()
        
        # Step 3: Pair smallest and largest elements and sum their GCDs
        total_sum = 0
        n = len(prefix_gcd)
        for i in range(n // 2):
            total_sum += get_gcd(prefix_gcd[i], prefix_gcd[n - 1 - i])
            
        return total_sum