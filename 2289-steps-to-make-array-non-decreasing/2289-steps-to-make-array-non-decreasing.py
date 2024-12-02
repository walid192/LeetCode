class Solution(object):
    def totalSteps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        stack = []
        max_steps = 0

        for num in nums:
            current_steps = 0
            while stack and stack[-1][0] <= num:
                current_steps = max(current_steps, stack.pop()[1])
            
            current_steps = current_steps + 1 if stack else 0
            max_steps = max(max_steps, current_steps)
            stack.append((num, current_steps))

        return max_steps
      
                
        
        