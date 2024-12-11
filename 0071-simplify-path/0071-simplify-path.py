from collections import deque
class Solution:
    def simplifyPath(self, path: str) -> str:
        
        directories=path.split('/')
        stack=[]
        
        for d in directories:
            if d=='.' or d=='':
                pass
            elif len(stack) and d=='..':
                stack.pop()
            elif d not in ['..']:
                stack.append(d)
                
        return '/'+('/'.join(stack))
            
                
        
        