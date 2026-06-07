class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.isupper():
            return True
        if word.islower():
            return True
        if len(word) > 1 and word[0].isupper() and word[1:].islower():
            return True

        return False