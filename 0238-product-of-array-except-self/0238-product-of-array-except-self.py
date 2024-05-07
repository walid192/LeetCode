class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer=[]
        def multiplyList(myList):
            result = 1
            for x in myList:
                result = result * x
            return result
        
        res=multiplyList(nums)
        
        for i in range(len(nums)):
            if(nums[i]==0):
                pref=nums[:i]
                suf=nums[i+1:]
                x,y=multiplyList(pref),multiplyList(suf)
                answer.append(x*y)
                
            else:
                answer.append(res/nums[i])
            
            
        return answer
            
            
        
        
        