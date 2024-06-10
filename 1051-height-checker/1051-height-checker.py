class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        count = [0] * 101
        for height in heights:
            count[height] += 1
        
        ans, j = 0, 0
        for i in range(len(heights)):
            while j < len(count) and count[j] == 0:
                j += 1
            if heights[i] != j:
                ans += 1
            count[j] -= 1
        return ans
        
