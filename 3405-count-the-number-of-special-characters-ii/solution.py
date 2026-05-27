class Solution(object):
    def numberOfSpecialChars(self, word):
        
        last_lower = {}
        first_upper = {}
        
        for i, char in enumerate(word):
            if char.islower():
                last_lower[char] = i
            else:
                lower_char = char.lower()
                if lower_char not in first_upper:
                    first_upper[lower_char] = i
                    
        special_count = 0
        for char in last_lower:
            if char in first_upper and last_lower[char] < first_upper[char]:
                special_count += 1
                
        return special_count
        
