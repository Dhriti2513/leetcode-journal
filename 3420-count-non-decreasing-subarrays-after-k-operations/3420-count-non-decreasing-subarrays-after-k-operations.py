class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        ops = 0
        q = deque()
        r = n - 1
        
        for l in range(n - 1, -1, -1):
            while q and nums[q[-1]] < nums[l]:
                idx = q.pop()
                next_idx = q[-1] if q else r + 1
                ops += (nums[l] - nums[idx]) * (next_idx - idx)
            q.append(l)
            
            while ops > k:
                ops -= nums[q[0]] - nums[r]
                if q[0] == r:
                    q.popleft()
                r -= 1
                
            ans += r - l + 1
            
        return ans