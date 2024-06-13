

class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        sortedStudents=sorted(students)
        sortedSeats=sorted(seats)
        
        total=0
        for i in range(len(students)):
            d=sortedStudents[i]-sortedSeats[i]
            total+=abs(d)
                
        return total