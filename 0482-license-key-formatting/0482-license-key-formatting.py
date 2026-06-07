class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        clean_s = s.replace("-", "").upper()

        if not clean_s:
            return""

        first_group_len = len(clean_s) % k
        res = []

        if first_group_len > 0:
            res.append(clean_s[:first_group_len])

        for i in range(first_group_len, len(clean_s), k):
            res.append(clean_s[i:i+k])

        return "-".join(res)