class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        count_zero_students = students.count(0)
        count_one_students = len(students) - count_zero_students
        
        count_zero_taken = 0
        count_one_taken = 0
        
        while sandwiches:
            if sandwiches[0] == 0: 
                if count_zero_taken < count_zero_students:
                    count_zero_taken += 1
                    sandwiches.pop(0)
                else:
                    break
            else:  
                if count_one_taken < count_one_students:
                    count_one_taken += 1
                    sandwiches.pop(0)
                else:
                    break
        
        return len(sandwiches)