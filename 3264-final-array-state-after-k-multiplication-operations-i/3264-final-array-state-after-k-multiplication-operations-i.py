class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        while(k>0):
            mini=min(nums)
            
            idx=nums.index(mini)
            nums[idx]*=multiplier
            k-=1
        return nums
        