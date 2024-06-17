class Solution(object):
        
    def judgeSquareSum(self, c):
        s, e = 0, int(sqrt(c))
        while(s <= e):
            p = s ** 2 + e ** 2
            if p == c: return True
            if p < c: s += 1
            else: e -= 1
        return False
        
        
        

   
        