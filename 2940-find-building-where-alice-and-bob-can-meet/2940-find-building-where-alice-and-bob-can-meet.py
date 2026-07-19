class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n = len(heights)
        q_len = len(queries)
        ans = [-1] * q_len
        deferred = [[] for _ in range(n)]
        
        # Step 1: Process queries and answer immediate cases
        for i, (a, b) in enumerate(queries):
            if a > b:
                a, b = b, a
            
            if a == b or heights[a] < heights[b]:
                ans[i] = b
            else:
                # Group by the larger index 'b', storing the required height and query index
                deferred[b].append((heights[a], i))
                
        # Step 2: Linear scan with a min-heap to resolve deferred queries
        min_heap = []
        for i in range(n):
            # Resolve all queries in the heap that are shorter than the current building
            while min_heap and min_heap[0][0] < heights[i]:
                _, q_idx = heapq.heappop(min_heap)
                ans[q_idx] = i
                
            # Push the deferred queries for the current building into the heap
            for req_height, q_idx in deferred[i]:
                heapq.heappush(min_heap, (req_height, q_idx))
                
        return ans