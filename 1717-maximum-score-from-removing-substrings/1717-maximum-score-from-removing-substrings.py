class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        def remove_substring(s, first, second, points):
            stack = []
            score = 0
            for char in s:
                if stack and stack[-1] == first and char == second:
                    stack.pop()
                    score += points
                else:
                    stack.append(char)
            return ''.join(stack), score
        
        if x > y:
            # Remove "ab" first
            s, score1 = remove_substring(s, 'a', 'b', x)
            s, score2 = remove_substring(s, 'b', 'a', y)
        else:
            # Remove "ba" first
            s, score1 = remove_substring(s, 'b', 'a', y)
            s, score2 = remove_substring(s, 'a', 'b', x)
        
        return score1 + score2
        