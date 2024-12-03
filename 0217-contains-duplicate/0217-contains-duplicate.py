class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        my_dict = {}
        
        for num in nums:
            if num in my_dict:
                return True
            
            else :
                my_dict[num]=1
                
        return False
        
        
        