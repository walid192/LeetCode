class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def calculComb(n):
            return n*(n-1)/2

        total=[]
        res=0
        for i,num in enumerate(nums):
            res+=num
            total.append(res%k)

        count=Counter(total)
        nb=0
        for c in count:
            if c!=0:
                 nb+=calculComb(count[c])
            else:
                 nb+=calculComb(count[c])+count[c]
             
        return int(nb) 
        
            
        
            
                
                
        