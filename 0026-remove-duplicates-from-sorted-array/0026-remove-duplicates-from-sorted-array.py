class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=0
        i=1
        while(i<len(nums)):
            if(nums[i]>nums[k]):
                k+=1
                nums[k]=nums[i]
            i+=1
        return k+1
                
                
                
            
            
        