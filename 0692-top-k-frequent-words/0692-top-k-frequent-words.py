class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        cnt=collections.Counter(words)
        sorted_values=sorted(cnt.items(),key=lambda x:(-x [1],x[0]),reverse=False)
        res= [key for key,_ in sorted_values[:k]]
        return res

        
        