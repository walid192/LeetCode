class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        i=0
        res=[]
        while(i<len(nums)):
            start=str(nums[i])
            while(i<len(nums)-1 and nums[i+1]==nums[i]+1):
                i+=1
            end=str(nums[i])
            
            if(start==end):
                res.append(start)
            else:
                res.append(start+'->'+end)
            i+=1
                
        return res
                
            
        