from bisect import bisect_left

class SegmentTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (4 * size)

    def update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
            return
        mid = (start + end) // 2
        if idx <= mid:
            self.update(2 * node, start, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, end, idx, val)
        self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, node, start, end, l, r):
        if l > end or r < start:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        p1 = self.query(2 * node, start, mid, l, r)
        p2 = self.query(2 * node + 1, mid + 1, end, l, r)
        return max(p1, p2)

class Solution(object):
    def getResults(self, queries):
        max_coord = 0
        for q in queries:
            max_coord = max(max_coord, q[1])
        
        limit = max_coord + 1
        
        obstacles = [0, limit]
        for q in queries:
            if q[0] == 1:
                obstacles.append(q[1])
        obstacles.sort()
        
        coord_to_idx = {val: i for i, val in enumerate(obstacles)}
        m = len(obstacles)
        
        seg_tree = SegmentTree(m)
        
        for i in range(1, m):
            gap = obstacles[i] - obstacles[i - 1]
            seg_tree.update(1, 0, m - 1, i, gap)
            
        results = []
        curr_obstacles = list(obstacles)
        
        for q in reversed(queries):
            if q[0] == 1:
                x = q[1]
                idx = bisect_left(curr_obstacles, x)
                
                prev_val = curr_obstacles[idx - 1]
                next_val = curr_obstacles[idx + 1]
                
                next_idx = coord_to_idx[next_val]
                seg_tree.update(1, 0, m - 1, next_idx, next_val - prev_val)
                
                curr_idx = coord_to_idx[x]
                seg_tree.update(1, 0, m - 1, curr_idx, 0)
                
                curr_obstacles.pop(idx)
                
            else:
                x, sz = q[1], q[2]
                
                idx = bisect_left(curr_obstacles, x)
                if idx < len(curr_obstacles) and curr_obstacles[idx] == x:
                    last_obstacle_before_x = x
                    right_bound_idx = coord_to_idx[x]
                else:
                    last_obstacle_before_x = curr_obstacles[idx - 1]
                    right_bound_idx = coord_to_idx[curr_obstacles[idx]] - 1
                
                max_gap = seg_tree.query(1, 0, m - 1, 0, right_bound_idx)
                max_gap = max(max_gap, x - last_obstacle_before_x)
                
                results.append(max_gap >= sz)
                
        return results[::-1]
        
        
        
