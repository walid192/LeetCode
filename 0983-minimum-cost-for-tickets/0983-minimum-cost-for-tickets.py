class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        travel_days = set(days)
        last_day = max(days)
        dp = [0] * (last_day + 2)

        for day in range(last_day, 0, -1):
            if day in travel_days:
                dp[day] = min(
                    dp[day + 1] + costs[0],
                    dp[day + 7] + costs[1] if day + 7 <= last_day else costs[1],
                    dp[day + 30] + costs[2] if day + 30 <= last_day else costs[2]
                )
            else:
                dp[day]=dp[day+1]
        return dp[1]