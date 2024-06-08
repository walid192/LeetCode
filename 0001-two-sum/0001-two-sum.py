class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        myMap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in myMap:
                return [myMap[complement], i]
            myMap[num] = i
            
            
            
            
            