class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        
        events=[]
        
        for num in nums:
            events.append((num-k,1))
            events.append((num+k+1,-1))
            
        events.sort()
        current=0
        maxi=0
        for value, effect in events:
            current+=effect
            maxi=max(maxi,current)
            
        return maxi
            
        
        
            