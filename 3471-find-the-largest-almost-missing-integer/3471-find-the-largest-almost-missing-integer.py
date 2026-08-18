class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        subarray_counts = Counter()
        for i in range(n - k + 1):
            window_unique = set(nums[i : i + k])
            for x in window_unique:
                subarray_counts[x] += 1
        candidates = [num for num, count in subarray_counts.items() if count == 1]
        
        return max(candidates) if candidates else -1