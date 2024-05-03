class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1_list=version1.split('.')
        version2_list=version2.split('.')
        equal=0
        i=0
        n=max(len(version1_list),len(version2_list))
        def compare_revision(i):
            rev1 = int(version1_list[i]) if i < len(version1_list) else 0
            rev2 = int(version2_list[i]) if i < len(version2_list) else 0
            if(rev1>rev2):
                return 1
            elif(rev1<rev2):
                return -1
            else:
                return 0
            
            
        while(equal==0 and i<n):
            equal=compare_revision(i)
            i+=1
        
        return equal
            