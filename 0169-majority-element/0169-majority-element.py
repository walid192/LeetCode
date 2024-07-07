class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        me=nums[0]
        count=0
        for i in range(len(nums)):
            if(nums[i]==me):
                count+=1
            else:
                count-=1
            if(count==0):
                me=nums[i]
                count=1
                
        if nums.count(me)>len(nums)//2:
            return me
            
        