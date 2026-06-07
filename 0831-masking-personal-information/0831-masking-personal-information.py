class Solution(object):
    def maskPII(self, s):
        """
        :type s: str
        :rtype: str
        """
        if '@' in s:
            name, domain = s.split('@')
            name = name.lower()
            domain = domain.lower()
            return name[0] + "*****" + name[-1] + "@" + domain
        else:
            digits = "".join([c for c in s if c.isdigit()])
            local = "***-***-" + digits[-4:]
            
            country_code_len = len(digits) - 10
            if country_code_len == 0:
                return local
            elif country_code_len == 1:
                return "+*-" + local
            elif country_code_len == 2:
                return "+**-" + local
            else:
                return "+***-" + local