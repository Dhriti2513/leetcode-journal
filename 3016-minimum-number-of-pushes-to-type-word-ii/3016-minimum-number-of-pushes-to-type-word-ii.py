class Solution:
    def minimumPushes(self, word: str) -> int:
        counts = Counter(word)
        
        # Step 2: Sort frequencies in descending order
        freqs = sorted(counts.values(), reverse=True)
        
        # Step 3: Calculate total pushes using greedy assignment
        total_pushes = 0
        for i, freq in enumerate(freqs):
            pushes_per_char = (i // 8) + 1
            total_pushes += freq * pushes_per_char
            
        return total_pushes