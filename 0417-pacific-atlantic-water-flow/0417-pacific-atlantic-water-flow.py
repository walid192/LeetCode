class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows,cols=len(grid),len(grid[0])

        pac,atl=set(),set()

        def dfs(r,c,s,prev):
            if r<0 or c<0 or r==rows or c==cols or grid[r][c]<prev or ((r,c))in s:
                return
            s.add((r,c))
            dfs(r+1,c,s,grid[r][c])
            dfs(r-1,c,s,grid[r][c])
            dfs(r,c+1,s,grid[r][c])
            dfs(r,c-1,s,grid[r][c])

        for r in range(rows):
            dfs(r,0,pac,grid[r][0])
            dfs(r,cols-1,atl,grid[r][cols-1])

        for c in range(cols):
            dfs(0,c,pac,grid[0][c])
            dfs(rows-1,c,atl,grid[rows-1][c])


        res=[]
        for i in range(rows):
            for j in range(cols):
                if (i,j) in pac and (i,j) in atl:
                    res.append([i,j])

        return res
        