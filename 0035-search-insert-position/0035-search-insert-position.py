class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,r=0,len(nums)-1

        while l<=r:
            median=(l+r)//2

            if nums[median]==target:
                return median
            elif nums[median]>target:
                r=median-1
            else:
                l=median+1

        return l
        