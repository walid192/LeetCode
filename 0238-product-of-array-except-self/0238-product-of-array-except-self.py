class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1]*len(nums)
        lprod = 1
        rprod = 1
        for i in range(len(nums)):
            res[i] *= lprod
            lprod *= nums[i]
            res[~i] *= rprod
            rprod *= nums[~i]
        return res
            
        
        
        