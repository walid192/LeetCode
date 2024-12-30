class Solution:
    def countGoodStrings(self, low: int, high: int, zeros: int, ones: int) -> int:

        MOD = 10**9 + 7 

        dp = [0] * (high + 1)
        dp[0] = 1  

        for length in range(high + 1):
            if dp[length] > 0:
                if length + zeros <= high:
                    dp[length + zeros] = (dp[length + zeros] + dp[length]) % MOD
                if length + ones <= high:
                    dp[length + ones] = (dp[length + ones] + dp[length]) % MOD

        return sum(dp[low:high + 1]) % MOD
