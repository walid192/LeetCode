class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        left,right=0,len(nums)-1

        while left<right:
            mid=(left+right)//2

            if nums[mid-1]<nums[mid] and nums[mid+1]<nums[mid]:
                return mid
            
            elif nums[mid+1]>nums[mid]:
                left=mid+1
            else:
                right=mid-1
        
        return left

        