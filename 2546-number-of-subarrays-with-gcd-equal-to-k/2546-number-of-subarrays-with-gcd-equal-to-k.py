import math
from functools import reduce

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        cnt = 0

        for i in range(len(nums)):
            current_gcd = 0
            for j in range(i, len(nums)):
                current_gcd = math.gcd(current_gcd, nums[j])
                if current_gcd == k:
                    cnt += 1
                elif current_gcd < k:
                    break
        
        return cnt