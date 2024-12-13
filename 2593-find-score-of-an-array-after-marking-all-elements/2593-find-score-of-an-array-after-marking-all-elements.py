import heapq

class Solution:
    def findScore(self, nums: List[int]) -> int:
        
        heap=[]
        seen=set()
        
        for i, num in enumerate(nums):
            heapq.heappush(heap, (num, i))          
        
        
        score=0
        
        while len(heap):
            smallest, idx = heapq.heappop(heap)
            
            
            if(idx in seen):
                continue
            
            score+=smallest
            seen.add(idx)
            if(idx>0):
                seen.add(idx-1)
            if (idx<len(nums)-1):
                seen.add(idx+1)
        
        return score
                