class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        
        # Step 1: Precompute LCM and sign for all 2^N - 1 non-empty subsets
        subsets = []
        for mask in range(1, 1 << n):
            current_lcm = 1
            size = 0
            for i in range(n):
                if (mask >> i) & 1:
                    current_lcm = math.lcm(current_lcm, coins[i])
                    size += 1
            
            sign = 1 if size % 2 == 1 else -1
            subsets.append((current_lcm, sign))
            
        # Helper function to count distinct amounts <= x
        def count_amounts(x: int) -> int:
            total = 0
            for lcm_val, sign in subsets:
                total += sign * (x // lcm_val)
            return total

        # Step 2: Binary Search for the k-th smallest amount
        low = 1
        high = min(coins) * k
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if count_amounts(mid) >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans