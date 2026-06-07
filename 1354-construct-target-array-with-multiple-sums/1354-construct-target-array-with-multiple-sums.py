import heapq

class Solution(object):
    def isPossible(self, target):
        """
        :type target: List[int]
        :rtype: bool
        """
        if len(target) == 1:
            return target[0] == 1
            
        total_sum = sum(target)
        max_heap = [-x for x in target]
        heapq.heapify(max_heap)
        
        while True:
            largest = -heapq.heappop(max_heap)
            if largest == 1:
                return True
                
            rest_sum = total_sum - largest
            
            if rest_sum == 1:
                return True
                
            if rest_sum == 0 or largest <= rest_sum:
                return False
                
            prev = largest % rest_sum
            if prev == 0:
                return False
                
            total_sum = rest_sum + prev
            heapq.heappush(max_heap, -prev)