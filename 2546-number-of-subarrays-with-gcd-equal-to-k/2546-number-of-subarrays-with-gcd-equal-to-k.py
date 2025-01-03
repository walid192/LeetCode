import math
from functools import reduce

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        
        cnt = 0
        # First loop to count single-element subarrays
        for num in nums:
            if math.gcd(num, k) == k:  # Fix: Added k as the second argument
                cnt += 1
        
        left, right = 0, 1
        while right < len(nums):
            result = reduce(math.gcd, nums[left:right+1])  # Fix: Corrected the use of reduce
            if result == k:
                print(nums[left:right+1])  # Debug print statement
                cnt += 1
                right += 1
            elif result > k:
                right += 1
            else:
                left += 1

            if left == right:  # Prevent infinite loop
                right += 1

        return cnt
            
            
            

