class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        sortedHeights=sorted(heights)
        nb=0
        for i in range(len(heights)):
            if (sortedHeights[i]!=heights[i]):
                nb+=1
                
        return nb
        
