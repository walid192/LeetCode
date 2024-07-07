class Solution(object):
    def numWaterBottles(self, b, e):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        nbre=0
        while(b>=e):
            d=b//e
            r=b%e
            nbre+=d*e
            b=r+d
        return nbre+b
