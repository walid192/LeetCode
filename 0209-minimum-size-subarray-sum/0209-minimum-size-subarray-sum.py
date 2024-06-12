class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left,total=0,0
        res=len(nums)+1
        
        for r in range(len(nums)):
            total+=nums[r]
            if( total>=target):
                while(total>=target):
                    res=min(res,r-left+1)
                    total-=nums[left]
                    left+=1
        return 0 if res==len(nums)+1 else res
                
                            
        
                
            