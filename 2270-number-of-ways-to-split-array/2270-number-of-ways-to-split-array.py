class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        pref=[0]*(len(nums)-1)
        pref[0]=nums[0]

        for i in range(1,len(pref)):
            pref[i]=pref[i-1]+nums[i]

        s=sum(nums)
        cnt=0
        for i in range(len(pref)):
            if (2*pref[i]>=s):
                cnt+=1
        return cnt


        