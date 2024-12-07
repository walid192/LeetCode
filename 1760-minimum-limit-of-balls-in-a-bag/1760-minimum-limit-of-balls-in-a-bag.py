class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def canAchievePenalty(penalty):
            operations = 0
            for num in nums:
                operations += (num - 1) // penalty
                if operations > maxOperations:
                    return False
            return True
        
        
        left,right=1,max(nums)

        while(left<=right):
            mid=(right+left)//2
            can=canAchievePenalty(mid)

            if(can):
                res=mid
                right=mid-1
            else:
                left=mid+1
        return res







        
         
       