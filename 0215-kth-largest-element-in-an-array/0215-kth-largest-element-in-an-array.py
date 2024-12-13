import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
            
        idx=0
        
        while(idx<k):
            res=heapq.heappop(max_heap)
            idx+=1
        
        return -res
            
            
        