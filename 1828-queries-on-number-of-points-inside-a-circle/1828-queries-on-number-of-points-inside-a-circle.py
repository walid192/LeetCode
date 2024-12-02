import math

class Solution(object):
    def countPoints(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        answer=[0]* len(queries)
        
        for point in points:
            for j, query in enumerate(queries):
                dis= math.sqrt(((query[0]-point[0])**2)+((query[1]-point[1])**2))
                if(dis<=query[2]):
                    answer[j]+=1
        
        return answer