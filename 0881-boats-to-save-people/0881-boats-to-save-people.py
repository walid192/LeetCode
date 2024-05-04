class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people=sorted(people,reverse=True)
        nb = 0  
        i, j = 0, len(people) - 1 
        while i <= j:
            if people[i] + people[j] <= limit:
                nb += 1
                i += 1 
                j -= 1 
            else:
                nb += 1
                i += 1  

        return nb
            
        