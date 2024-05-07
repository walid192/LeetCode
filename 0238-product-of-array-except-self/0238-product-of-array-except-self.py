class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        prod = 1
        for x in nums:
            prod *= x if x != 0 else 1
        count0 = nums.count(0)
        for x in nums:
            if count0 > 1: 
                ans.append(0)
            elif count0 == 1:
                ans.append(prod if x == 0 else 0)
            else:
                ans.append(prod//x)
        return ans   
            
            
        
        
        