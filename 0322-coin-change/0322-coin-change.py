class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:


        dp=[-1]*(amount+1)

        dp[0] = 0
        for i in range(1, amount + 1):
            m = float('inf')
            for coin in coins:
                if i >= coin and dp[i - coin] != -1:
                    m = min(m, dp[i - coin] + 1)
            dp[i] = m if m != float('inf') else -1

        return dp[amount] if dp[amount] != -1 else -1