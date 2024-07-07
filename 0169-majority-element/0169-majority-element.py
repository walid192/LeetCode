class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sortedNums=sorted(nums)
        return sortedNums[len(nums)//2]
        