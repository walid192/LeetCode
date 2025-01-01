class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_score = 0
        best_prev = values[0]  

        for j in range(1, len(values)):
            max_score = max(max_score, best_prev + values[j] - j)

            best_prev = max(best_prev, values[j] + j)

        return max_score
        