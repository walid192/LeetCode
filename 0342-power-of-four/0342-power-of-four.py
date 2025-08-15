class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        result = math.log(n) / math.log(4)
        if abs(result - round(result)) < 1e-10:
            return True
        return False
        