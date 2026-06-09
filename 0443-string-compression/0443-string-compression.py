class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        write = 0
        read = 0
        length = len(chars)
        
        while read < length:
            char = chars[read]
            count = 0
            
            while read < length and chars[read] == char:
                read += 1
                count += 1
                
            chars[write] = char
            write += 1
            
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
                    
        return write