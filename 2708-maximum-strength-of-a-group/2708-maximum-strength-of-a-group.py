class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        contains_zero = False
        positive = []
        negative = []

        for num in nums:
            if num > 0:
                positive.append(num)
            elif num < 0:
                negative.append(num)
            else:
                contains_zero = True

        if len(negative) & 1:
            if len(negative) > 1:
                negative.remove(max(negative))
            elif positive:
                return prod(positive)
            elif contains_zero:
                return 0
            else:
                return max(negative)

        if not (negative or positive):
            return 0

        return prod(negative) * prod(positive)
        