class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        digit_counts = Counter(digits)
        valid_count = 0
        for num in range(100, 1000, 2):
            d1, d2, d3 = num // 100, (num // 10) % 10, num % 10
            req = Counter([d1, d2, d3])
            
            if all(digit_counts[d] >= count for d, count in req.items()):
                valid_count += 1
                
        return valid_count