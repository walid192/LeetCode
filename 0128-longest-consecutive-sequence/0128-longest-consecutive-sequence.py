class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        setNums=set(nums)
        longest=0
        
        for n in nums:
            if(n-1 )not in setNums:
                length=0
                while(n+length in setNums):
                    length+=1
                longest=max(longest,length)
                
        return longest