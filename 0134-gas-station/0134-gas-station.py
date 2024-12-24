class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        total_tank = 0  # Total gas available across the entire circuit
        current_tank = 0  # Current gas in the tank while iterating
        start_station = 0  # Starting gas station index
        
        for i in range(len(gas)):
            # Calculate net gas at station `i`
            net_gas = gas[i] - cost[i]
            total_tank += net_gas
            current_tank += net_gas
            
            # If current tank is negative, reset starting point
            if current_tank < 0:
                start_station = i + 1  # Start from the next station
                current_tank = 0  # Reset current tank
        
        # If total gas is negative, a complete circuit is not possible
        return start_station if total_tank >= 0 else -1
                
        
        