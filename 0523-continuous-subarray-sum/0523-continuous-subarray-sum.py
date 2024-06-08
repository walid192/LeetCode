class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        reminderMap={0:-1}
        total=0
        for i in range(len(nums)):
            total+=nums[i]
            reminder=total % k
            if reminder in reminderMap:
                if i-reminderMap.get(reminder)>1:
                    return True
            else:
                reminderMap[reminder]=i
        return False

        