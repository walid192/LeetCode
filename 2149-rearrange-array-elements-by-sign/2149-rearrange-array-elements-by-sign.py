class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        posQueue=collections.deque()
        negQueue=collections.deque()
        
        for num in nums:
            if num>0:
                posQueue.append(num)
            else:
                negQueue.append(num)

        res=[]
        
        while(posQueue or negQueue):
            p=posQueue.popleft()
            n=negQueue.popleft()

            res.append(p)
            res.append(n)

        return res
