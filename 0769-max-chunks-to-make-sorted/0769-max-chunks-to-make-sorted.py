class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        if len(arr) <= 1:
            return 1

        chunks=0
        maxi=float('-inf')
        
        for i,num in enumerate(arr):
            maxi=max(maxi,num)
            if i==maxi:
                chunks+=1
                
        return chunks