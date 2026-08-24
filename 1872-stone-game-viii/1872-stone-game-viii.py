class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        pref = stones[:]
        for i in range(1, n):
            pref[i] += pref[i - 1]
        ans = pref[-1]
        for i in range(n - 2, 0, -1):
            ans = max(ans, pref[i] - ans)
            
        return ans