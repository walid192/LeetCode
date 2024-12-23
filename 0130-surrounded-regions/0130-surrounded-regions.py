class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        if not board:
            return board
        
        rows,cols=len(board),len(board[0])
        visited=set()
        
        
        def bfs(r,c):
            queue=collections.deque()
            queue.append((r,c))
            
            while queue:
                r,c=queue.popleft()
                
                directions=[[1,0],[-1,0],[0,1],[0,-1]]
                
                for dr,dc in directions:
                    if( r+dr in range(rows)
                       and c+dc in range(cols) 
                       and board[r+dr][c+dc]=='O'
                       and (r+dr,c+dc) not in visited):
                        visited.add((r+dr,c+dc))
                        queue.append((r+dr,c+dc))
                        
        
        
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=='O' and ((c==0 or c==cols-1) or(r==0 or r==rows-1 )):
                    visited.add((r,c))
                    bfs(r,c)
                    
        for r in range(rows-1):
            for c in range(cols-1):
                if board[r][c]=='O' and (r,c) not in visited:
                    board[r][c]='X'
                    
                    
       
        