class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)
        
        # 1. Count occurrences of each number
        cnt = [0] * (max_val + 1)
        for num in nums:
            cnt[num] += 1
            
        # 2. Count total numbers divisible by each i
        total_multiples = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            for j in range(i, max_val + 1, i):
                total_multiples[i] += cnt[j]
                
        # 3. Compute count of pairs with exact gcd = i using inclusion-exclusion backwards
        gcd_count = [0] * (max_val + 1)
        for i in range(max_val, 0, -1):
            c = total_multiples[i]
            pairs = c * (c - 1) // 2
            
            # Subtract pairs where the GCD is a strict multiple of i
            sub = 0
            for j in range(2 * i, max_val + 1, i):
                sub += gcd_count[j]
                
            gcd_count[i] = pairs - sub
            
        # 4. Construct prefix sums of the gcd counts
        prefix_sums = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            prefix_sums[i] = prefix_sums[i - 1] + gcd_count[i]
            
        # 5. Answer each query using binary search
        ans = []
        for q in queries:
            idx = bisect.bisect_right(prefix_sums, q)
            ans.append(idx)
            
        return ans
        