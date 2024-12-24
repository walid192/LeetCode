class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        def reachStart(position):
            if position == 0:
                return True
            
            for i in range(position - 1, -1, -1):
                if i + nums[i] >= position:
                    return reachStart(i)
            
            return False
        
        return reachStart(len(nums) - 1)
            
        
        