class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j=1
        
        for i in range(2,len(nums)):
            if nums[i]!=nums[j-1]:
                j+=1
                nums[j]=nums[i]
                
        return j+1