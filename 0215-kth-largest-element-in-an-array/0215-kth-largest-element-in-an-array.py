import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap=[]
        
        
        for num in nums:
            heapq.heappush(heap,num)
            
        idx=len(nums)-k
        
        while(idx>=0):
            res=heapq.heappop(heap)
            idx-=1
        
        return res
            
            
        