class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        rev_s = s[::-1]
        temp = s + "#" + rev_s
        n = len(temp)
        lps = [0] * n
        
        for i in range(1, n):
            j = lps[i - 1]
            while j > 0 and temp[i] != temp[j]:
                j = lps[j - 1]
            if temp[i] == temp[j]:
                j += 1
            lps[i] = j
        palindrome_prefix_len = lps[-1]
        remaining_suffix = s[palindrome_prefix_len:]
        return remaining_suffix[::-1] + s