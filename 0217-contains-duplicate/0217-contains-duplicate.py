class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        my_set=set(nums)
        return len(nums)>len(my_set)
        