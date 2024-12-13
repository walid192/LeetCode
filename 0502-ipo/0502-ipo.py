import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        my_list = list(zip(profits, capital))
        sorted_values = sorted(my_list, key=lambda x: x[1])
        
        max_heap = []
        i = 0 
        
        for _ in range(k):
            while i < len(sorted_values) and sorted_values[i][1] <= w:
                profit, _ = sorted_values[i]
                heapq.heappush(max_heap, -profit)
                i += 1
            
            if max_heap:
                w -= heapq.heappop(max_heap)  
            else:
                break
        
        return w

                
            
        
        
        
        
            
        
        