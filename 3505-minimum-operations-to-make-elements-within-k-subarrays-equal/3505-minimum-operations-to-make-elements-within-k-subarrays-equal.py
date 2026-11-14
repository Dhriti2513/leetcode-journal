class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        m = n - x + 1
        costs = [0] * m
        
        low = []
        high = []
        low_sum = 0
        high_sum = 0
        delayed = {}
        low_size = 0
        high_size = 0
        
        def prune(heap, is_low):
            while heap:
                val = -heap[0] if is_low else heap[0]
                if delayed.get(val, 0) > 0:
                    delayed[val] -= 1
                    heappop(heap)
                else:
                    break
                    
        def rebalance():
            nonlocal low_size, high_size, low_sum, high_sum
            if low_size > high_size + 1:
                val = -heappop(low)
                low_size -= 1
                low_sum -= val
                heappush(high, val)
                high_size += 1
                high_sum += val
                prune(low, True)
            elif high_size > low_size:
                val = heappop(high)
                high_size -= 1
                high_sum -= val
                heappush(low, -val)
                low_size += 1
                low_sum += val
                prune(high, False)
                
        def add(val):
            nonlocal low_size, high_size, low_sum, high_sum
            if not low or val <= -low[0]:
                heappush(low, -val)
                low_size += 1
                low_sum += val
            else:
                heappush(high, val)
                high_size += 1
                high_sum += val
            rebalance()
            
        def remove(val):
            nonlocal low_size, high_size, low_sum, high_sum
            delayed[val] = delayed.get(val, 0) + 1
            if val <= -low[0]:
                low_size -= 1
                low_sum -= val
                if val == -low[0]:
                    prune(low, True)
            else:
                high_size -= 1
                high_sum -= val
                if high and val == high[0]:
                    prune(high, False)
            rebalance()
            
        for i in range(n):
            add(nums[i])
            if i >= x:
                remove(nums[i - x])
            if i >= x - 1:
                median = -low[0]
                costs[i - x + 1] = (median * low_size - low_sum) + (high_sum - median * high_size)
                
        INF = float('inf')
        dp = [0] * (m + 1)
        
        for _ in range(1, k + 1):
            new_dp = [INF] * (m + 1)
            for i in range(m - 1, -1, -1):
                take = costs[i] + (dp[i + x] if i + x <= m else (0 if _ == 1 else INF))
                new_dp[i] = min(new_dp[i + 1], take)
            dp = new_dp
            
        return dp[0]