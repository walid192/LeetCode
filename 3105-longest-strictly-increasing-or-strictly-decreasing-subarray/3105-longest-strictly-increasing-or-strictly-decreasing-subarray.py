class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        res = 1  

        i = 0
        while i < n:
            inc_len = 1
            while i + 1 < n and nums[i] < nums[i + 1]:
                inc_len += 1
                i += 1
            res = max(res, inc_len)

            dec_len = 1
            while i + 1 < n and nums[i] > nums[i + 1]:
                dec_len += 1
                i += 1
            res = max(res, dec_len)
            
            i += 1  

        return res