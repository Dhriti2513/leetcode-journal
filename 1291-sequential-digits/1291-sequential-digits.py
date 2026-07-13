class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        sample = "123456789"
        res = []
        for length in range(len(str(low)), len(str(high)) + 1):
            for start in range(10 - length):
                num = int(sample[start:start + length])
                if low <= num <= high:
                    res.append(num)
                    
        return res