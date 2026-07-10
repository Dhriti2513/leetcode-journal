from bisect import bisect_right

class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        sorted_nodes = sorted((nums[i], i) for i in range(n))
        sorted_vals = [val for val, idx in sorted_nodes]
        
        pos_in_sorted = [0] * n
        for sorted_pos, (val, orig_idx) in enumerate(sorted_nodes):
            pos_in_sorted[orig_idx] = sorted_pos
            
        comp = [0] * n
        curr_comp = 0
        for i in range(1, n):
            if sorted_vals[i] - sorted_vals[i - 1] > maxDiff:
                curr_comp += 1
            comp[i] = curr_comp
            
        LOG = n.bit_length()
        up = [[0] * n for _ in range(LOG)]
        
        for i in range(n):
            right_idx = bisect_right(sorted_vals, sorted_vals[i] + maxDiff) - 1
            up[0][i] = right_idx
            
        for k in range(1, LOG):
            for i in range(n):
                up[k][i] = up[k - 1][up[k - 1][i]]
                
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
                
            pos_u = pos_in_sorted[u]
            pos_v = pos_in_sorted[v]
            
            if comp[pos_u] != comp[pos_v]:
                ans.append(-1)
                continue
                
            if pos_u > pos_v:
                pos_u, pos_v = pos_v, pos_u
                
            if up[0][pos_u] >= pos_v:
                ans.append(1)
                continue
                
            steps = 0
            for k in range(LOG - 1, -1, -1):
                if up[k][pos_u] < pos_v:
                    steps += (1 << k)
                    pos_u = up[k][pos_u]
                    
            ans.append(steps + 1)
            
        return ans