from collections import defaultdict
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen=defaultdict(list)
        
        for i,num in enumerate(nums):
            if num in seen:
                last_index=seen[num][-1]
                if(abs(last_index-i))<=k:
                    return True
                
            seen[num].append(i)
        
        return False
        