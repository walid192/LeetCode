class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])

        if m==1 and n==1: return 0

        arr=[]

        for i in range(m):
            arr+=grid[i]

        arr.sort()

        cand1=arr[len(arr)//2]
        cand2=arr[len(arr)//2-1]

        def getMinOps(target):
            ans = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if abs(grid[i][j]-target)%x!=0:
                        return -1
                    else:
                        ans+=abs(grid[i][j]-target)//x

            return ans

        return min(getMinOps(cand1),getMinOps(cand2))


