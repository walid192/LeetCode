class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        top, bottom = 0, len(matrix) - 1
        while top <= bottom:
            middle = (top + bottom) // 2
            if matrix[middle][0] <= target <= matrix[middle][-1]:
                left, right = 0, len(matrix[middle]) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if matrix[middle][mid] == target:
                        return True
                    elif matrix[middle][mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                return False  
            elif matrix[middle][0] > target:
                bottom = middle - 1
            else:
                top = middle + 1
        
        return False