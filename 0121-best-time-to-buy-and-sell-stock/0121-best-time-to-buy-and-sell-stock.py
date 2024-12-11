class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i,j=0,1
        mx_profit=0
        
        while(j<len(prices)):
            profit=prices[j]-prices[i]
            mx_profit=max(profit,mx_profit)
            if (prices[j]<prices[i]):
                i+=1
                j=i+1
            else:
                j+=1
                
        return mx_profit            
            
        