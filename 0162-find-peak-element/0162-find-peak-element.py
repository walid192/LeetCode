class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return 0
        if nums[0]>nums[1]:
            return 0
        if nums[-1]>nums[-2]:
            return len(nums)-1

        l,r=0,len(nums)-1
        while l<=r:
            med=(l+r)//2

            if nums[med-1]<nums[med] and nums[med]>nums[med+1]:
                return med

            elif nums[med]<nums[med+1]:
                l=med+1
            else:
                r=med-1
        