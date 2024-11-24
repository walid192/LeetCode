class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_sum = 0
        min_abs_value = float('inf')
        negative_count = 0
        
        for row in matrix:
            for num in row:
                total_sum += abs(num)  
                if num < 0:
                    negative_count += 1 
                min_abs_value = min(min_abs_value, abs(num)) 
                
        if negative_count % 2 == 1:
            total_sum -= 2 * min_abs_value
        
        return total_sum
        