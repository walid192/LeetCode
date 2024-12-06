class Solution(object):
    def minimalKSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(set(nums))
        result = 0
        prev = 0

        for num in nums:
            if num - prev > 1:
                count = min(k, num - prev - 1)
                if count > 0:
                    start = prev + 1
                    end = prev + count
                    result += (end * (end + 1)) // 2 - (start * (start - 1)) // 2
                    k -= count
            prev = num

            if k == 0:
                return result

        if k > 0:
            start = prev + 1
            end = prev + k
            result += (end * (end + 1)) // 2 - (start * (start - 1)) // 2

        return result
            
        