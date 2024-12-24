class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pref=[]
        rev_pref=[]
        
        reversed_nums=nums[::-1]
        
        product = 1
        for i in range(len(nums)):
            pref.append(product)
            product *= nums[i]
        
        product = 1
        for j in range(len(reversed_nums)):
            rev_pref.append(product)
            product *= reversed_nums[j]
        
        rev_pref = rev_pref[::-1]  
        
        res = []
        for i in range(len(nums)):
            res.append(pref[i] * rev_pref[i])
        
        return res
            
        
            