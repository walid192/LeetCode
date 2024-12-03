from collections import defaultdict

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        my_dict = defaultdict(int)
        for num in nums:
            my_dict[num]+=1
            if(my_dict[num]>1):
                return True
            
        return False
        
        
        