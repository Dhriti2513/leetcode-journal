class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        time = 0
        target_tickets = tickets[k]
        
        for i in range(len(tickets)):
            if i <= k:
                time += min(tickets[i], target_tickets)
            else:
                time += min(tickets[i], target_tickets - 1)
                
        return time