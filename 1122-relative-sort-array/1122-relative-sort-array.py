from collections import Counter
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        count=Counter(arr1)
        j=0
        for i,num in enumerate(arr2):
            nbOccu=count[num]
            for i in range(nbOccu):
                arr1[i+j]=num
            j+=nbOccu
            del count[num]
        sortedKeys=sorted(count.keys())
        for key in sortedKeys:
            nbOccu=count[key]
            for i in range(nbOccu):
                arr1[i+j]=key
            j+=nbOccu


        return(arr1)
