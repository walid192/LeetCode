class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        max_length = 0
        visited = set()

        for num in nums:
            if num not in visited:
                current_length = 1
                visited.add(num)
                prev, next_num = num - 1, num + 1

                while prev in nums:
                    visited.add(prev)
                    prev -= 1
                    current_length += 1

                while next_num in nums:
                    visited.add(next_num)
                    next_num += 1
                    current_length += 1

                max_length = max(max_length, current_length)

        return max_length