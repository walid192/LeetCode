class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        candidate=None
        for num in nums:
            if count==0:
                candidate=num
            count+=(1 if candidate==num else -1)
        candidate

        if nums.count(candidate)>len(nums)//2:
            return candidate
            
        