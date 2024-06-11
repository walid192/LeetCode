class Solution(object):
    def twoSum(self, n, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i=0
        j=len(n)-1
        res=[]
        while(i<j):
            somme=n[i]+n[j]
            if(somme==target):
                res.append(i+1)
                res.append(j+1)
                return res
            elif (somme>target):
                j-=1
            else:
                i+=1