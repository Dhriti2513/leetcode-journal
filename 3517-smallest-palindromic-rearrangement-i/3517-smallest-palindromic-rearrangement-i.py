class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        half_len = n // 2
        
        # Step 1: Sort the characters in the first half
        left = "".join(sorted(s[:half_len]))
        
        # Step 2: Extract middle character if length is odd
        mid = s[half_len] if n % 2 != 0 else ""
        
        # Step 3: Construct the palindrome
        return left + mid + left[::-1]