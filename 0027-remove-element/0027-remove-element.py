from collections import Counter

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count=Counter(nums)
        k=len(nums)
        if(val in count):
            k=len(nums)-count[val]

        for i,num in enumerate(nums):
            if (num)==val:
                nums[i]=float('+inf')    

        nums.sort() 
        return k 
        
        