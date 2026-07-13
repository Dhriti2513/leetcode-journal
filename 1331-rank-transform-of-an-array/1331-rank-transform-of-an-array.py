class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        rank_map = {val: rank for rank, val in enumerate(sorted(set(arr)), 1)}
        return [rank_map[x] for x in arr]