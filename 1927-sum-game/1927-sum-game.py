class Solution:
    def sumGame(self, num: str) -> bool:
        half_len = len(num) // 2
        
        left_str = num[:half_len]
        right_str = num[half_len:]
        
        s1 = sum(int(ch) for ch in left_str if ch != '?')
        q1 = left_str.count('?')
        
        s2 = sum(int(ch) for ch in right_str if ch != '?')
        q2 = right_str.count('?')
        
        return 2 * (s1 - s2) != 9 * (q2 - q1)