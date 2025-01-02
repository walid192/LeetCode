class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:


        mxy=min(x,y)

        if x==y:
            return 2*x+2*y+2*z

        else:
            return 4*mxy+2*z+2
            

    