class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        count_zero_students = students.count(0)
        count_one_students = len(students) - count_zero_students
        
        # Initialize variables to keep track of how many students of each type have taken sandwiches
        count_zero_taken = 0
        count_one_taken = 0
        
        # Simulate students taking sandwiches or going to the end of the queue
        while sandwiches:
            if sandwiches[0] == 0:  # Circular sandwich
                if count_zero_taken < count_zero_students:
                    count_zero_taken += 1
                    sandwiches.pop(0)
                else:
                    break
            else:  # Square sandwich
                if count_one_taken < count_one_students:
                    count_one_taken += 1
                    sandwiches.pop(0)
                else:
                    break
        
        # Return the number of students unable to eat (remaining in the queue)
        return len(sandwiches)