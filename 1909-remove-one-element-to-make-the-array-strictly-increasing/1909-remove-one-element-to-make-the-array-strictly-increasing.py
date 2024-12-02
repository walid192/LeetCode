class Solution(object):
    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        violations = 0
        
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                violations += 1
                if violations > 1:
                    return False
                
                if i > 1 and nums[i] <= nums[i - 2]:
                    nums[i] = nums[i - 1]
        
        return True
            
            
        