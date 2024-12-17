from collections import Counter
import heapq
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        cnt = Counter(s)
        heap = []
        res = []
        
        for char, freq in cnt.items():
            heapq.heappush(heap, (-ord(char), freq))
        
        while heap:
            char_ord, freq = heapq.heappop(heap)
            char = chr(-char_ord)
            
            write_limit = min(freq, repeatLimit)
            res.append(char * write_limit)
            freq -= write_limit
            
            if freq > 0:
                if not heap:
                    break 
                
                next_char_ord, next_freq = heapq.heappop(heap)
                next_char = chr(-next_char_ord)
                
                res.append(next_char)
                next_freq -= 1
                
                if next_freq > 0:
                    heapq.heappush(heap, (next_char_ord, next_freq))
                
                heapq.heappush(heap, (char_ord, freq))
        
        return ''.join(res)