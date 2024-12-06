class Solution(object):
    def maxCount(self, banned, n, maxSum):
        """
        :type banned: List[int]
        :type n: int
        :type maxSum: int
        :rtype: int
        """
        my_set=set(banned)
        s=0
        output=0
        
        for i in range(1,n+1):
            if i not in my_set and s+i<=maxSum:
                s+=i
                output+=1
            
        return output


        