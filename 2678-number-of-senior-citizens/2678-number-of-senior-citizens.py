class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        nb=0
        for detail in details:
            if int(detail[11:13])>60:
                nb+=1
                
        return nb
        