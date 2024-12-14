from sortedcontainers import SortedList
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        window = SortedList()
        left = 0
        result = 0

        for right in range(len(nums)):
            window.add(nums[right])

            while window[-1] - window[0] > 2:
                window.remove(nums[left])
                left += 1

            result += (right - left + 1)

        return result
        