from collections import Counter
class Solution(object):
    def canChange(self, start, target):
        """
        :type start: str
        :type target: str
        :rtype: bool
        """ 
        s_counter=Counter(start)
        t_counter=Counter(target)
#         check if they have same number of R and L
        
        if(s_counter!=t_counter):
            return False
        
        
#         check if the two words after compressing are the same:
        s_compressed= start.replace('_','')
        t_compressed=target.replace('_','')
        if(s_compressed!=t_compressed):
            return False
        
        s_positions = [(char, i) for i, char in enumerate(start) if char in 'LR']
        t_positions = [(char, i) for i, char in enumerate(target) if char in 'LR']
        

        for (s_char, s_index), (t_char, t_index) in zip(s_positions, t_positions):
            if s_char == 'L' and t_index > s_index: 
                return False
            if s_char == 'R' and t_index < s_index: 
                return False

        return True



