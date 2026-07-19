class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_occ = {char: i for i, char in enumerate(s)}
        
        stack = []
        seen = set()
        
        for i, char in enumerate(s):
            # Skip the character if it's already included in our current subsequence
            if char in seen:
                continue
                
            # Maintain a lexicographically smallest order:
            # Pop characters from the stack if they are larger than the current char
            # AND we know they appear again later in the string.
            while stack and stack[-1] > char and last_occ[stack[-1]] > i:
                seen.remove(stack.pop())
                
            stack.append(char)
            seen.add(char)
            
        return "".join(stack)