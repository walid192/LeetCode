class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
            
        my_dict={}
        
        for i,str in enumerate(strs):
            sorted_str=''.join(sorted(str))
            
            if(sorted_str)in my_dict:
                my_dict[sorted_str].append(str)
            else:
                 my_dict[sorted_str]=[str]
                    
        res=[]
        for value in my_dict.values():
            res.append(value)
        return res
            

            
                   
        