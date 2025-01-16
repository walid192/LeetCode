class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos_index=0
        neg_index=1
        arr=[0]*(len(nums))

        for i in range(len(nums)):
            if nums[i]>0:
                arr[pos_index]=nums[i]
                pos_index+=2
            else:
                arr[neg_index]=nums[i]
                neg_index+=2

        return arr
