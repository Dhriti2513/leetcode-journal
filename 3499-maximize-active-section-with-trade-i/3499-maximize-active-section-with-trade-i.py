class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        total_ones = s.count('1')
        
        # Step 1: Collect lengths of all contiguous zero-blocks
        zero_blocks = []
        curr_len = 0
        
        for char in s:
            if char == '0':
                curr_len += 1
            else:
                if curr_len > 0:
                    zero_blocks.append(curr_len)
                    curr_len = 0
        if curr_len > 0:
            zero_blocks.append(curr_len)
            
        # Step 2: If fewer than 2 zero-blocks exist, no trade can be made
        if len(zero_blocks) < 2:
            return total_ones
            
        # Step 3: Find maximum sum of two adjacent zero-block lengths
        max_gain = 0
        for i in range(len(zero_blocks) - 1):
            max_gain = max(max_gain, zero_blocks[i] + zero_blocks[i + 1])
            
        return total_ones + max_gain