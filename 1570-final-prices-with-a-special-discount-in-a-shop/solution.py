class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        answer = list(prices)
        stack = []
        
        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                prev_index = stack.pop()
                answer[prev_index] -= prices[i]
            stack.append(i)
            
        return answer
