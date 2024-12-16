class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        res=[]
        sorted_values=sorted(intervals,key=lambda x: x[0])
        
        res.append(sorted_values[0])
        for i,value in enumerate(sorted_values[1:]):
            
            if value[0]<=res[-1][1]:
                start=res[-1][0]
                end=max(value[1],res[-1][1])
                res[-1]=[start,end]
            else:
                res.append(value)
        return res
                
                
        
        
            
            
            
        
        
        