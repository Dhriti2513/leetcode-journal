class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        if n <= 3:
            return 1

        s = [1, 2, 2]
        head = 2

        while len(s) < n:
            next_char = 1 if s[-1] == 2 else 2
            repeat_times = s[head]
            s.extend([next_char] * repeat_times)
            head += 1
        return s[:n].count(1)