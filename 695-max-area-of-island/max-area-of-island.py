class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]==0:
                return 0
            else:
                grid[i][j]=0
                area=1
                area+=dfs(i,j+1)
                area+=dfs(i+1,j)
                area+=dfs(i,j-1)
                area+=dfs(i-1,j)
            return area    
        num_islands=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    num_islands=max(num_islands,dfs(i,j))
                    dfs(i,j)
        return num_islands         
        