class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_seen = {'a': -1, 'b': -1, 'c': -1}
        total_substrings = 0
        
        for r, char in enumerate(s):
            last_seen[char] = r
            if last_seen['a'] != -1 and last_seen['b'] != -1 and last_seen['c'] != -1:
                total_substrings += min(last_seen['a'], last_seen['b'], last_seen['c']) + 1
        return total_substrings